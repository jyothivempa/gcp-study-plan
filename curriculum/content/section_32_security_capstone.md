# SECTION 32: Security Capstone (Red Team Audit)

## 🕵️‍♂️ The Scenario
You are a Security Engineer auditing a "Shadow IT" project created by a junior developer.
The project is "Working", but it is a **Security Nightmare**.

## 1️⃣ The "Bad" Architecture
```mermaid
graph TD
    User[Any User] --"Access"--> Bucket[Storage Bucket: Public Read/Write]
    Dev[Developer] --"Key.json"--> VM[VM Instance]
    VM --"Admin Access"--> Project[Project Owner Role]
    
    style Bucket fill:#fee2e2,stroke:#991b1b
    style VM fill:#fee2e2,stroke:#991b1b
```

## 2️⃣ The Objectives
1.  **Identify:** Find 3 Critical Vulnerabilities.
2.  **Remediate:** Lock them down using CLI.
3.  **Verify:** Confirm access is Denied for unauthorized users.

## 3️⃣ Lab Steps (Guided) 🛠️

### Step 1: Reconnaissance
Run these commands to find the holes.
1.  `gcloud projects get-iam-policy [PROJECT_ID]`
    *   *Look for:* `roles/owner` on a Service Account.
    *   *Look for:* `keys` downloaded to local machines (simulated).
2.  `gcloud storage buckets get-iam-policy gs://[BUCKET_NAME]`
    *   *Look for:* `allUsers` having `roles/storage.objectAdmin`.

### Step 3: The Job-Ready Solution (Terraform) 🛡️
Auditing is hard. Hardening via code is better. Save this as `main.tf`.

```hcl
# main.tf
# 1. Custom Role (Least Privilege)
resource "google_project_iam_custom_role" "auditor_role" {
  role_id     = "app_auditor"
  title       = "App Auditor"
  description = "Can view logs and monitoring, but cannot edit resources."
  permissions = [
    "logging.logEntries.list",
    "logging.logs.list",
    "monitoring.timeSeries.list",
    "compute.instances.get",
    "compute.instances.list"
  ]
}

# 2. Service Account (Identity)
resource "google_service_account" "app_sa" {
  account_id   = "sa-app-prod"
  display_name = "Production Application Service Account"
}

# 3. Bind Role to Service Account
resource "google_project_iam_binding" "app_permissions" {
  project = "your-project-id"
  role    = google_project_iam_custom_role.auditor_role.name
  members = ["serviceAccount:${google_service_account.app_sa.email}"]
}
```
**Why this wins interviews:** You show you understand *custom roles* reducing the attack surface, rather than lazy `roles/viewer` assignments.

## 4️⃣ Checkpoint Questions
**Q1. You see a bucket policy granting `roles/storage.objectViewer` to `allUsers`. What does this mean?**
*   A. Only authenticated Google users can view.
*   B. Only users in your organization can view.
*   C. Anyone on the entire internet can view.
*   D. It is disabled.
> **Answer: C.** "allUsers" = The Public Internet.

**Q2. Why is granting `roles/owner` to a VM Service Account bad?**
*   A. It costs more money.
*   B. If the VM is hacked, the attacker owns the entire project (can delete everything).
*   C. It slows down the VM.
*   D. It works fine.
> **Answer: B.** Blast Radius. Always use Least Privilege.

**Q3. How do you SSH into a VM without opening Port 22 to the world?**
*   A. Use a VPN.
*   B. Use IAP (Identity-Aware Proxy).
*   C. Use RDP.
*   D. Use Telnet.
> **Answer: B.** IAP tunnels traffic through Google's HTTPS load balancers, authenticating you before you reach the VM.
