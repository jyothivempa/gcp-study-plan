# SECTION 21: Putting It All Together (Architecture Thinking)

## 1️⃣ Plain-English Explanation
We have all the Lego bricks: Compute, Storage, Network, SQL, Security.
**Architecture** is building the castle.
On the exam, you won't get asked "What is a VM?"
You will get asked: "A customer needs a fault-tolerant web app that stores relational data and images. It must be cheap."
*   *Translation:*
    *   Fault-tolerant Web App -> **Managed Instance Group (Autoscaling)** or **Cloud Run**.
    *   Relational Data -> **Cloud SQL**.
    *   Images (Unstructured) -> **Cloud Storage**.
    *   Cheap -> **Standard Storage** + **Preemptible VMs** (if applicable).

## 2️⃣ Common Patterns (The "Exam Blueprint")
1.  **Strict Compliance (Banks):**
    *   Compute: **Sole-Tenant Nodes**.
    *   Storage: **Regional** (Specific Country) Buckets.
    *   Key: **Private Google Access** (No Public IPs).
    *   Encryption: **CMEK** (Customer Managed Encryption Keys).
2.  **Global Scalability (Netflix-style):**
    *   Frontend: **Global HTTP(S) Load Balancer**.
    *   Compute: **MIGs** in multiple regions.
    *   Database: **Cloud Spanner**.
3.  **Cheap Static Website (Marketing):**
    *   **Cloud Storage Bucket** (Public, Website ON).
    *   **Cloud CDN** (for speed).
    *   *No VMs. No Database.*

## 3️⃣ The Elimination Strategy 🧠
When you see a complex question:
1.  **Eliminate the "Fake" Services:** (e.g., "Google Relational Store" -> Fake).
2.  **Eliminate the "Wrong Scope":** (e.g., Question says "Global DB", Answer says "Cloud SQL" -> Wrong. Cloud SQL is Regional).
3.  **Eliminate the "Wrong Type":** (e.g., Question says "Unstructured Data", Answer says "BigQuery" -> Wrong. BigQuery is for Analytics/Structured).

## 4️⃣ One-Line Memory Hook 🧠
> "Architecture is just **Matching Requirements** to **Capabilities**."

## 5️⃣ Checkpoint Questions
1.  **Requirement: Millisecond latency for gaming. Global users. UDP traffic.**
    *   *Solution: Network Load Balancer + Compute Engine.*
2.  **Requirement: Store 1PB of sensor logs. Query them using SQL. Low cost.**
    *   *Solution: BigQuery.*
3.  **Requirement: Run a Python script every night at 2 AM.**
    *   *Solution: Cloud Scheduler + Cloud Functions (or Cloud Run Jobs).*

## ➡️ What’s Next 
This is it. You have the knowledge. Now we test it.
**Next Section:** The 30-Day Final Exam.



## ⚡ Zero-to-Hero: Pro Tips
*   **CLI Command**: Practice `gcloud final list` to see resources via command line.
*   **Real World**: In production, prefer **Terraform** over clicking in the console for final.


<!-- FLASHCARDS
[
  {
    "term": "Well-Architected",
    "def": "Framework for building secure, efficient, resilient systems."
  },
  {
    "term": "Decoupling",
    "def": "Separating components so failure doesn't cascade (using Pub/Sub)."
  },
  {
    "term": "Statelessness",
    "def": "Apps that don't store session data locally. Easy to scale."
  },
  {
    "term": "Blue/Green",
    "def": "Deployment strategy with two environments to minimize downtime."
  },
  {
    "term": "Circuit Breaker",
    "def": "Pattern to stop calling a failing service to prevent overload."
  }
]
-->
