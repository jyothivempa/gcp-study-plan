
# 🛠️ Lab 14: IAM & Service Account Troubleshooting

**Objective:** Understand Service Account permissions by breaking and fixing access to a Bucket.
**Duration:** 20 Minutes

## 1. Setup Resources
Create a VM and a Bucket.

```bash
# 1. Create a Bucket (Must be globally unique)
BUCKET_NAME="iam-lab-${GOOGLE_CLOUD_PROJECT}-${RANDOM}"
gsutil mb gs://$BUCKET_NAME/

# 2. Upload a secret file
echo "Top Secret Data" > secret.txt
gsutil cp secret.txt gs://$BUCKET_NAME/

# 3. Create a Service Account
gcloud iam service-accounts create my-lab-sa --display-name "Lab SA"

# 4. Create a VM using this Service Account
gcloud compute instances create iam-test-vm \
    --zone=us-central1-a \
    --service-account=my-lab-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com \
    --scopes=cloud-platform
```

## 2. Verify "Access Denied" (The Problem)
The Service Account has **NO roles** by default.
1.  SSH into the VM:
    ```bash
    gcloud compute ssh iam-test-vm --zone=us-central1-a
    ```
2.  Try to read the bucket:
    ```bash
    # Replace BUCKET_NAME with your actual bucket name
    gsutil ls gs://<YOUR_BUCKET_NAME>
    ```
3.  **Result:** `AccessDeniedException: 403 access denied`.

## 3. Grant Permissions (The Fix)
Exit the SSH session (`exit`).
Grant the `Storage Object Viewer` role to the Service Account.

```bash
# Get SA Email
SA_EMAIL=my-lab-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com

# Grant Role
gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
    --member="serviceAccount:${SA_EMAIL}" \
    --role="roles/storage.objectViewer"
```

## 4. Verify Success
1.  SSH into the VM again.
2.  Run `gsutil ls gs://<YOUR_BUCKET_NAME>`
3.  **Result:** Success! You can see `secret.txt`.

## 5. Least Privilege Challenge
What if we want to *write* a file?
Try: `touch test.txt && gsutil cp test.txt gs://<YOUR_BUCKET_NAME>/`
**Result:** **Access Denied!** Why?
*   We gave `Object Viewer` (Read-only).
*   To fix, you would need `Object Creator` or `Object Admin`.

## 🧹 Cleanup
```bash
gcloud compute instances delete iam-test-vm --zone=us-central1-a --quiet
gcloud iam service-accounts delete $SA_EMAIL --quiet
gsutil rm -r gs://$BUCKET_NAME
```
