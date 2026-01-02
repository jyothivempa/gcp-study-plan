# SECTION 27: Cloud Build & CI/CD Pipelines

> **Official Doc Reference**: [Cloud Build](https://cloud.google.com/build/docs)

## 1️⃣ What is CI/CD?
*   **CI (Continuous Integration):** "I push code -> Tests run automatically."
*   **CD (Continuous Deployment):** "Tests pass -> App updates in production automatically."

**Cloud Build** is GCP's Serverless CI/CD platform. It's like Jenkins, but you don't manage the server.

## 2️⃣ How Cloud Build Works
1.  **Triggers:** Listen for git push events (GitHub, Bitbucket, Cloud Source Repos).
2.  **Steps:** A list of Docker containers. Each step runs a command.
3.  **Artifacts:** Validated images/jars stored in Artifact Registry.

## 3️⃣ The `cloudbuild.yaml` File
This is the heart of the pipeline.

```yaml
steps:
# Step 1: Build the Docker image
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/my-app', '.']

# Step 2: Push to Artifact Registry
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'gcr.io/$PROJECT_ID/my-app']

# Step 3: Deploy to Cloud Run
- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
  entrypoint: gcloud
  args: ['run', 'deploy', 'my-service', '--image', 'gcr.io/$PROJECT_ID/my-app', '--region', 'us-central1']

images:
- 'gcr.io/$PROJECT_ID/my-app'
```

## 4️⃣ Hands-On Lab: Build & Push 🏗️

**Scenario:** We will manually trigger a build to creating a container image.

### Step 1: Enable APIs
```bash
gcloud services enable cloudbuild.googleapis.com artifactregistry.googleapis.com
```

### Step 2: Create a Dockerfile
```bash
# Create a dummy app
echo "FROM python:3.9-slim" > Dockerfile
echo "RUN echo 'Hello World'" >> Dockerfile
```

### Step 3: Submit the Build
```bash
gcloud builds submit --tag gcr.io/${PROJECT_ID}/quickstart-image .
```

### Step 4: Verify
1.  Go to **Cloud Build > History**. You should see a green checkmark.
2.  Go to **Artifact Registry (or Container Registry)**. You should see your image.

## 5️⃣ Advanced: Worker Pools (Private Pools)
By default, Cloud Build runs on Google's public infrastructure.
If you need to access a private GKE cluster or a database in a private VPC, you need **Private Pools**.
*   **Peered Network:** Allows Cloud Build to reach private IPs.

## 6️⃣ Exam Tips 💡
1.  **"Speed up builds"** = Use Kaniko cache or larger machine types (`machineType: 'N1_HIGHCPU_8'`).
2.  **"Access private VPC"** = Use Cloud Build Private Pools.
3.  **"Automate deployment on git tag"** = Use Cloud Build Triggers with regex filter `^v\d+\.\d+\.\d+$`.

## 7️⃣ Checkpoint Questions

**Q1. You want to deploy to a GKE Private Cluster using Cloud Build. The build fails because it cannot reach the cluster control plane. What do you do?**
*   A. Grant Owner role to Cloud Build.
*   B. **Use Cloud Build Private Pools peered to the VPC.**
*   C. Open firewall 0.0.0.0/0.
> **Answer: B.** Private GKE clusters have no public endpoint. Public Cloud Build cannot reach them without peering.

**Q2. Which file defines the build steps?**
*   A. Dockerfile
*   B. **cloudbuild.yaml**
*   C. autoscale.yaml
> **Answer: B.** Dockerfile defines the image; cloudbuild.yaml defines the pipeline.

## ✅ Day 27 Checklist
<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I submitted a manual build using gcloud.', checked: false },
        { text: 'I understand the structure of cloudbuild.yaml.', checked: false },
        { text: 'I know when to use Private Pools.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 27 Checklist
    </h3>
    <template x-for="(item, index) in items" :key="index">
        <div class="checklist-item" @click="item.checked = !item.checked">
            <div class="checklist-box" :class="{ 'checked': item.checked }">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
            </div>
            <span x-text="item.text" :class="{ 'line-through text-slate-400': item.checked }"></span>
        </div>
    </template>
</div>
