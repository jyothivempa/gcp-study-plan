# SECTION 12: IAM Fundamentals

> **Official Doc Reference**: [IAM Documentation](https://cloud.google.com/iam/docs)

## 1️⃣ Overview: The "Who, What, Where" principle
Identity and Access Management (IAM) is the gatekeeper of Google Cloud. It essentially validates three questions:
1.  **Who** are you? (Identity)
2.  **What** do you want to do? (Role/Permission)
3.  **Where** do you want to do it? (Resource)

## 2️⃣ Architecture Diagram: The Inheritance Waterfall
Permissions in GCP flow **DOWN**.
*   **Rule:** If you are an Editor on the *Parent*, you are an Editor on *All Children*.
*   **Implication:** You cannot "Restrict" access at a lower level if it was granted higher up (mostly).

```mermaid
graph TD
    Org[🏢 Organization (Root)]
    FolderHR[📂 Folder: HR]
    FolderDev[📂 Folder: IT/Dev]
    ProjA[📦 Project A: Production]
    ProjB[📦 Project B: Staging]
    Bucket[🪣 Storage Bucket]
    
    User[👤 User: Alice]
    
    Org --> FolderHR
    Org --> FolderDev
    FolderDev --> ProjA
    FolderDev --> ProjB
    ProjA --> Bucket
    
    User --"Granted 'Editor' Role Here"--> FolderDev
    
    style FolderDev fill:#dbeafe,stroke:#1e40af
    style ProjA fill:#dcfce7,stroke:#15803d
    style ProjB fill:#dcfce7,stroke:#15803d
    style Bucket fill:#fef3c7,stroke:#d97706
```
*   **Visual Logic:** Because Alice is an Editor on the **IT Folder**, she automatically has full Edit access to **Project A**, **Project B**, and the **Bucket**. She doesn't need to be added to them individually.

## 3️⃣ IAM Policy Structure (The JSON)
An IAM Policy is a collection of Bindings.
```json
{
  "bindings": [
    {
      "role": "roles/storage.objectViewer",
      "members": [
        "user:bob@example.com",
        "group:dev-team@example.com"
      ]
    }
  ]
}
```

## 4️⃣ Roles: Primitive vs Predefined vs Custom (Table)

| Role Type | Example | Description | **Use Case** |
| :--- | :--- | :--- | :--- |
| **Primitive** | `Owner`, `Editor` | Grants broad access to EVERYTHING. | **Sandbox / PoC Only.** Never use in Prod. |
| **Predefined** | `roles/storage.admin` | Granular access managed by Google. | **Standard.** Use this for 99% of tasks. |
| **Custom** | `my-custom-role` | User-picked permissions. | **Advanced.** Use only if Predefined doesn't fit. |

## 5️⃣ Zero-to-Hero: IAM Conditions ⚡
**Scenario:** You want Alice to be a "Project Editor", but **ONLY** if she logs in from the corporate VPN IP address.
**Solution:** IAM Conditions (Attribute-Based Access Control).

*   **Logic:**
    *   **Role:** Editor
    *   **Condition:** `request.time < 18:00` AND `request.access_levels.contains("Corp_VPN")`
    *   **Result:** Alice is an Editor at work. At home, she is nobody.

## 6️⃣ Hands-On Lab: Debugging Access 🕵️‍♂️
**Scenario:** Bob says "I cannot view the bucket, but you gave me the right role!"

### Step 1: Check Hierarchy
Did you grant the role on `Project-A`, but the bucket is actually inside `Project-B`?

### Step 2: Policy Troubleshooter
1.  Go to IAM > **Policy Troubleshooter**.
2.  Input:
    *   **Principal:** `bob@example.com`
    *   **Resource:** `//storage.googleapis.com/my-bucket`
    *   **Permission:** `storage.objects.get`
3.  **Result:** It will visualize exactly WHICH role (or lack thereof) is causing the Deny.

## 7️⃣ Exam Traps 🚨
*   **Trap:** "I need to deny 'User A' from accessing a specific bucket, but allow them access to the rest of the project."
    *   *Answer:* You cannot easily "Deny" in standard IAM v1. You must **NOT GRANT** the permission at the project level. Grant it at the resource level for everyone *except* User A. (Or use IAM Deny Policies v2, but standard exam logic prefers "Least Privilege at Grant Time").
*   **Trap:** "Which identity is best for a script running on a VM?"
    *   *Answer:* **Service Account**. Never use a user's Gmail password or credentials in code.

## 8️⃣ Checkpoint Questions (Exam Style)
**Q1. You need to grant a diverse team (Devs, QAs, PMs) access to a project. People join and leave weekly. What is the Google Best Practice?**
*   A. Add each user individually to the IAM Policy.
*   B. Create a generic shared account `dev@gmail.com`.
*   C. Use **Google Groups**. Map IAM roles to Groups, not Users.
*   D. Use Primitive roles for simplicity.
> **Answer: C.** Groups scaling. You manage membership in G-Suite/Cloud Identity, and IAM stays clean.

**Q2. Which tool helps you visualize why a user DOES or DOES NOT have access?**
*   A. Cloud Logging
*   B. Policy Troubleshooter
*   C. VPC Flow Logs
*   D. Security Command Center
> **Answer: B.** Policy Troubleshooter is purpose-built for this.

**Q3. True or False: If I grant "Viewer" at the Organization level, I can block that access at the Project level.**
*   A. True
*   B. False
> **Answer: B.** Permissions are additive. You inherit the Union of all roles. You cannot subtract permissions as you go down (without using advanced Deny policies).
