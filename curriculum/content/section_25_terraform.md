# SECTION 25: Infrastructure as Code (Terraform)

> **Official Doc Reference**: [Terraform on Google Cloud](https://cloud.google.com/docs/terraform)

## 1️⃣ Overview: Click-Ops vs Code
*   **Click-Ops:** Manually clicking in the console. Error-prone. Unrepeatable. "It works on my machine."
*   **Infrastructure as Code (IaC):** Writing a text file (`main.tf`) that describes your resources.
    *   **Tool:** **Terraform** (HashiCorp) is the industry standard.
    *   **Benefit:** Version Control (Git). Peer Review for infrastructure changes.

## 2️⃣ The Terraform Workflow (The Holy Trinity)

```mermaid
graph TD
    Write[1. Write Code (main.tf)] --> Init[2. terraform init]
    Init --> Plan[3. terraform plan]
    
    Plan --"Preview Changes"--> Review{User Review}
    Review --"Approve"--> Apply[4. terraform apply]
    Review --"Reject"--> Write
    
    Apply --"API Calls"--> GCP[Google Cloud Platform]
    
    style Plan fill:#fef3c7,stroke:#d97706
    style Apply fill:#dcfce7,stroke:#15803d
```

## 3️⃣ Key Concepts: State & Modules
1.  **State File (`terraform.tfstate`):** The "Brain".
    *   It records the mapping between your code and the Real World (e.g., `resource "google_storage_bucket" "my_bucket"` = ID `bkt-12345`).
    *   *Pro Tip:* Store this in **Cloud Storage** (Remote Backend), not on your laptop.
2.  **Modules:** Reusable blueprints.
    *   Instead of writing 100 lines for a VPC, use `module "vpc"`.

## 4️⃣ Zero-to-Hero: Google Cloud Foundation Toolkit ⚡
Don't write everything from scratch. Google provides "Best Practice" blueprints.
*   **Google Logic:** "Don't just create a VM. Create a VM with Shielded OS, Private IP, and No External Access."
*   These modules bake security in by default.

## 5️⃣ Hands-On Lab: Deploy a Bucket 🪣
1.  **Write `main.tf`:**
    ```hcl
    provider "google" {
      project = "my-project"
      region  = "us-central1"
    }
    
    resource "google_storage_bucket" "auto-expire" {
      name          = "my-tf-bucket-${random_id.suffix.hex}"
      location      = "US"
      force_destroy = true
    }
    ```
2.  **Run:**
    `terraform init`
    `terraform apply`
3.  **To Destroy:**
    `terraform destroy`

## 6️⃣ Exam Traps 🚨
*   **Trap:** "I changed a resource in the Google Console manually. Now Terraform is failing."
    *   *Answer:* This is **Drift**. Terraform expects the world to match the State file. You should revert the manual change or run `terraform refresh`.
*   **Trap:** "How do I import an existing VM into Terraform management?"
    *   *Answer:* Use `terraform import`. It pulls the ID into the state file.
*   **Trap:** "Where should I store the state file for a team of 5 engineers?"
    *   *Answer:* **Cloud Storage (GCS)** with Object Versioning enabled (for backup) and State Locking (to prevent collisions).

## Checkpoint Questions

**Q1. Which command shows you what Terraform *will* do before it actually does it?**
*   A. `terraform apply`
*   B. `terraform plan`
*   C. `terraform init`
*   D. `terraform preview`
> **Answer: B.** Always run plan first!

**Q2. Why is it dangerous to commit `terraform.tfstate` to Git?**
*   A. It is too large.
*   B. It acts as a binary.
*   C. It may contain **secrets** (passwords/keys) in plain text.
*   D. Git doesn't support .tfstate files.
> **Answer: C.** Even if you use variables, the raw values are often stored in the state file.

**Q3. Which Terraform feature allows you to reuse a set of resources (e.g., "Web Server Standard Config") multiple times?**
*   A. Workspaces
*   B. Modules
*   C. Providers
*   D. Outputs
> **Answer: B.** Modules are the functions of IaC.
