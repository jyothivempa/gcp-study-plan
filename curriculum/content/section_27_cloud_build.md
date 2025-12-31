# SECTION 27: Cloud Build (CI/CD)

> **Official Doc Reference**: [Cloud Build Documentation](https://cloud.google.com/build/docs)

## 1️⃣ Overview: Serverless CI/CD
*   **Concept:** "I have code in GitHub. I want to build a Docker image and deploy it to Cloud Run."
*   **The Tool:** **Cloud Build**. It's effectively "Serverless Jenkins".
*   **The Cost:** 120 free build-minutes/day.

## 2️⃣ Architecture: The Pipeline

```mermaid
graph LR
    Dev[Developer] --"git push"--> GitHub[GitHub Repo]
    GitHub --"Trigger"--> CloudBuild[Cloud Build]
    
    subgraph "Cloud Build Steps"
        Step1[1. Run Unit Tests (Python)]
        Step2[2. Build Container (Docker)]
        Step3[3. Push to Registry (Artifact Registry)]
        Step4[4. Deploy (Cloud Run)]
        
        Step1 --> Step2 --> Step3 --> Step4
    end
    
    Step4 --"Live URL"--> Prod[Production]
    
    style CloudBuild fill:#dbeafe,stroke:#1e40af
    style Step3 fill:#fef3c7,stroke:#d97706
```

## 3️⃣ The `cloudbuild.yaml` Anatomy 🧬
This file lives in your root directory. It tells Google what to do.
```yaml
steps:
  # Step 1: Run Tests
  - name: 'python:3.9'
    entrypoint: 'bash'
    args: ['-c', 'pip install pytest && pytest']

  # Step 2: Build Image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/my-app', '.']

  # Step 3: Deploy
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: 'gcloud'
    args: ['run', 'deploy', 'my-app', '--image', 'gcr.io/$PROJECT_ID/my-app', '--region', 'us-central1']

images:
  - 'gcr.io/$PROJECT_ID/my-app'
```

## 4️⃣ Zero-to-Hero: Private Pools 🏊‍♂️
*   **Default Pool:** Your build runs on a public, shared Google VM. It has **No Access** to your private VPC resources (like a Private Database).
*   **Private Pool:** You pay to provision dedicated workers **peered** to your VPC.
    *   *Use Case:* "My build tests need to talk to a private SQL database."

## 5️⃣ Exam Traps 🚨
*   **Trap:** "I need to speed up my build. It downloads the same pip packages every time."
    *   *Answer:* Use **Kaniko** cache or Cloud Storage caching. Cloud Build is ephemeral (fresh VM every time).
*   **Trap:** "My build fails because it can't reach an external API that requires a static IP."
    *   *Answer:* Use **Private Pools** with a dedicated Static IP (Cloud NAT).
*   **Trap:** "How do I secure my build secrets (API keys)?"
    *   *Answer:* Use **Secret Manager**.
        *   `secretEnv: ['MY_API_KEY']` in `cloudbuild.yaml`.

## 6️⃣ Checkpoint Questions (Exam Style)
**Q1. Where does Cloud Build execute your build steps by default?**
*   A. On your local laptop.
*   B. On a shared, ephemeral Google Worker VM.
*   C. On your GKE cluster.
*   D. Inside your App Engine instance.
> **Answer: B.** It's serverless and temporary.

**Q2. You want to trigger a build automatically whenever code is pushed to the "main" branch. What do you verify?**
*   A. Create a Cron Job.
*   B. Create a **Cloud Build Trigger** connected to the GitHub repository.
*   C. Run `gcloud builds submit` manually.
*   D. Send an email to Google.
> **Answer: B.** Triggers listen for webhook events from GitHub/Bitbucket.

**Q3. Your security team says: "Builds must never run on public infrastructure." What feature do you use?**
*   A. Shielded VMs.
*   B. Binary Authorization.
*   C. **Private Pools**.
*   D. VPC Flow Logs.
> **Answer: C.** Private pools ensure isolation and VPC connectivity.
