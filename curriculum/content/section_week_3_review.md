
# WEEK 3 REVIEW: Security, IAM & Serverless

## 1️⃣ WEEK 3 ANALOGY CHEAT SHEET (The "Basics")
We covered a lot of advanced ground this week. Here is the translation guide:

| Concept | Technical Term | Analogy | Why? |
| :--- | :--- | :--- | :--- |
| **IAM Service Account** | `serviceAccount` | **Robot Badge** | Humans have passwords. Robots (Apps/VMs) have badges (Keys). |
| **App Engine** | `PaaS` | **Serviced Apartment** | You live in it (Code), Google maintains the building (OS/Scale). |
| **Cloud Run** | `Serverless Containers` | **Pop-up Food Truck** | Appears instantly for customers (Requests), vanishes when empty. Cheap. |
| **Kubernetes (GKE)** | `Orchestration` | **City Planner** | You provide the blueprints (Manifests), GKE builds and repairs the city. |
| **Cloud Logging** | `Cloud Logging` | **Security Camera** | Records everything that happens (Who did what, Errors). |
| **Cloud Monitoring** | `Metrics/Alerts` | **Dashboard / Alarm** | The siren that rings when the building is on fire (CPU > 90%). |

## 2️⃣ Mental Map Recap
1.  **Identity (IAM):** The foundation. Who can do what?
2.  **Compute Options:**
    *   **VM (Compute Engine):** DIY House.
    *   **Container (GKE/Run):** Prefab Modules.
    *   **App Engine:** Serviced Apartment.
    *   **Functions:** Glue.


## 6️⃣ Hands-On Lab: The "Security Audit" Challenge
**Mission:** Verify who has access to your project.

1.  **Open Cloud Shell**.
2.  **List all Service Accounts:**
    ```bash
    gcloud iam service-accounts list
    ```
3.  **Check Project IAM Policy:**
    ```bash
    gcloud projects get-iam-policy [YOUR_PROJECT_ID] --format="table(bindings.role, bindings.members)"
    ```
4.  **Identify Risks:** Look for `roles/editor` assigned to `allUsers` (Bad!) or default service accounts used in prod.

## 7️⃣ Checkpoint Questions (IAM & Security Mock Exam)


**Q1. You need to give a consultant read-only access to a specific Cloud Storage bucket. You do not want them to see anything else in the project. What should you do?**
*   A. Assign roles/viewer at the Project level.
*   B. Assign roles/storage.objectViewer at the Bucket level.
*   C. Create a Service Account for them.
*   D. Assign roles/owner at the Bucket level.
> **Correct Answer: B.** *Least Privilege requires scoping access to the specific resource (Bucket) and specific action (Viewer).*

**Q2. Your application running on a VM needs to write data to BigQuery. What is the most secure method to authenticate?**
*   A. Embed a Service Account JSON key in the source code.
*   B. Store the JSON key in a text file on the VM.
*   C. Create a Service Account with the BigQuery Data Editor role and attach it to the VM.
*   D. Use your personal Gmail account credentials.
> **Correct Answer: C.** *Attaching a Service Account allows the VM to use "Application Default Credentials" without managing key files.*

**Q3. You want to receive an email notification whenever a specific error message appears in your application logs. Which tool should you use?**
*   A. Cloud Monitoring (Alerting Policy) based on a Log-based Metric.
*   B. Cloud Trace.
*   C. Cloud Profiler.
*   D. VPC Flow Logs.
> **Correct Answer: A.** *You convert a Log entry into a Metric, then Alert on that Metric.*

**Q4. Who is responsible for securing the underlying physical hardware of the data center?**
*   A. You (The Customer).
*   B. Google.
*   C. Both (Shared Responsibility).
*   D. The ISP.
> **Correct Answer: B.** *In the Shared Responsibility Model, Google owns physical security.*

**Q5. A user left your company. You deleted their Google Account. What happens to the IAM policies that referenced that user?**
*   A. They act as "orphaned" entries but effectively deny access since the user doesn't exist.
*   B. The policies are automatically deleted.
*   C. The Project is suspended.
*   D. The user can still log in.
> **Correct Answer: A.** *The policy entries remain (cleaning them up is manual work), but the user cannot log in.*

**Q6. Which command would you use to list all the VMs in your project?**
*   A. `gcloud compute instances list`
*   B. `gcloud vm show`
*   C. `kubectl get pods`
*   D. `gsutil ls`
> **Correct Answer: A.** *Standard gcloud syntax: Service (compute) > Resource (instances) > Verb (list).*

**Q7. You need to store audit logs for 7 years to meet compliance regulations. What should you do?**
*   A. Do nothing; Cloud Logging keeps them forever.
*   B. Create a Log Sink to export logs to a Cloud Storage bucket with an Archive lifecycle policy.
*   C. Print them out.
*   D. Export them to BigQuery.
> **Correct Answer: B.** *Archive Storage is the most cost-effective solution for long-term retention.*

**Q8. What is the difference between a Role and a Permission?**
*   A. They are the same.
*   B. A Role contains many Permissions. You assign Roles to users.
*   C. A Permission contains many Roles.
*   D. Permissions are for users; Roles are for robots.
> **Correct Answer: B.** *You cannot assign a raw Permission (e.g., compute.instances.start) directly to a user.*

**Q9. Provide the CLI command to initialize the configuration (login, set project/region).**
*   A. `gcloud start`
*   B. `gcloud login`
*   C. `gcloud init`
*   D. `gcloud config set`
> **Correct Answer: C.** *gcloud init runs a wizard to set up everything.*

**Q10. Can you restrict an IAM Role to be active only during working hours (e.g., 9 AM to 5 PM)?**
*   A. No, IAM is permanent.
*   B. Yes, using IAM Conditions.
*   C. Only for Billing roles.
*   D. Yes, by using a cron job to delete the user every night.
> **Correct Answer: B.** *IAM Conditions allows you to add logic (Time, Date, IP) to allowance policies.*

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I know the difference between a Principal, a Role, and a Policy.', checked: false },
        { text: 'I know WHY using JSON keys is dangerous (and what to do instead).', checked: false },
        { text: 'I can write a basic Log-Based Alert.', checked: false },
        { text: 'I passed the mock exam (8/10).', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Confidence Checklist
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

**READY?**
If you passed, get ready for **Week 4: Serverless & Data**. We are leaving infrastructure behind and moving to pure code!



<!-- FLASHCARDS
[
  {
    "term": "Week 3 Focus",
    "def": "Serverless and Compute Options."
  },
  {
    "term": "GKE vs Cloud Run",
    "def": "GKE = Complex orchestration. Cloud Run = Simple container serving."
  },
  {
    "term": "App Engine vs Cloud Functions",
    "def": "App Engine = Full App. Functions = Snippets of code."
  },
  {
    "term": "Cloud Build",
    "def": "CI/CD service to build containers."
  },
  {
    "term": "Ops Agent",
    "def": "Software installed on VM to send logs/metrics to Google."
  }
]
-->
