# SECTION 15: Cloud Shell & gcloud CLI

## 1️⃣ Plain-English Explanation
*   **Console (Web UI):** Click-ops. Good for viewing, learning, and one-off tasks. "Driving Automatic."
*   **CLI (gcloud):** Script-ops. Good for bulk action, automation, and precision. "Driving Manual."
*   **Cloud Shell:** A free, disposable Linux computer that Google gives you inside your browser.

## 2️⃣ The "gcloud" Anatomy
Every command follows a specific grammar:
`gcloud [GROUP] [SUBGROUP] [ACTION] [The Thing] --[flags]`

*   **Group:** `compute` (Virtual Machines), `storage` (Buckets), `iam` (Permissions).
*   **Example Translation:**
    *   `gcloud compute instances create my-vm` -> "Hey Google, use the Compute service to create an instance named my-vm."

## 3️⃣ Cloud Shell Ecosystem (Diagram)
What actually happens when you click the `>_` icon?

```mermaid
graph TD
    Browser[Your Browser] --Websocket (Port 443)--> GoogleFE[Google Front End]
    GoogleFE --> Container[Cloud Shell VM (e2-small)]
    
    subgraph "Your Personal Space"
        Container --> HomeDir[/$HOME (5GB Persistent Disk)]
        Container --> Tools[Pre-installed: gcloud, git, docker, java, python, terraform]
        Container --> Auth[Auto-Auth (You are already logged in)]
    end
    
    style HomeDir fill:#dcfce7,stroke:#15803d
    style Tools fill:#dbeafe,stroke:#1e40af
```
*   **Key Value:** You don't need to install Python, Terraform, or Docker. It's already there.

## 4️⃣ The "Power User" Cheatsheet 🤖
Memorize these 5 patterns to look like a pro.

| Pattern | Command | Use Case |
| :--- | :--- | :--- |
| **The "Who Am I?"** | `gcloud auth list` | Check which account is active. |
| **The "Where Am I?"** | `gcloud config list project` | Check which project you are touching. |
| **The "Switch Projects"** | `gcloud config set project [ID]` | Switch context. |
| **The "Output JSON"** | `gcloud ... --format=json` | Get raw data for parsing. |
| **The "Filter"** | `gcloud ... --filter="status=RUNNING"` | Search for specific resources. |

## 5️⃣ Scripting: The Bash Loop
**Scenario:** Create 10 Buckets.
*   *The "Click" way:* 50 clicks. 5 minutes.
*   *The "Shell" way:* 3 lines. 5 seconds.
```bash
for i in {1..10}; do
  gcloud storage buckets create gs://test-bucket-$i-$RANDOM --location=us-central1
done
```

## 6️⃣ Exam Traps 🚨
*   **Trap:** "I installed the SDK on my laptop. I try to run a command and it says 'Authentication Required'. What do I do?"
    *   *Answer:* Run `gcloud init` (Initializes config and logs you in via browser).
*   **Trap:** "Where are my files stored if I restart Cloud Shell?"
    *   *Answer:* Only files in `$HOME` (Home Directory) are saved. Files in `/usr` or `/tmp` are lost.

## 7️⃣ Checkpoint Questions (Exam Style)
**Q1. Which flag allows you to filter the output of a gcloud list command?**
*   A. `--search`
*   B. `--grep`
*   C. `--filter`
*   D. `--find`
> **Answer: C.** e.g., `gcloud compute instances list --filter="name=web-server"`.

**Q2. True or False: You check out a git repository in Cloud Shell. You close the tab and come back next week. Is the code still there?**
*   A. Yes, if it was in the Home Directory.
*   B. No, the VM is ephemeral.
*   C. Only if you clicked "Save".
> **Answer: A.** The Home Directory is persistent storage.

**Q3. How do you switch the active project in gcloud?**
*   A. `gcloud project switch`
*   B. `gcloud config set project [ID]`
*   C. `gcloud switch [ID]`
*   D. `gcloud use [ID]`
> **Answer: B.** We modify the `config` property.
