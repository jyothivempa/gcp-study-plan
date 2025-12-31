# SECTION 29: Architect Case Studies (Thinking Like a Pro)

> **Goal**: Synthesize everything you've learned (Networking + Compute + Data + Security).

## 1️⃣ Scenario A: The "Uber" Clone 🚕
**Requirement:**
*   Global scale (US, Europe, Asia).
*   Real-time Location tracking (Driver updates lat/long every 5s).
*   Payment processing (Strong consistency).
*   Analytics (Surge pricing calculation).

**The Solution:**
*   **Compute:** **GKE** (Microservices for Matchmaking, User Profile).
*   **Real-Time Data:** **Pub/Sub** (Ingest location pings) -> **Dataflow** (Process/Filter) -> **Bigtable** (Store location history).
*   **Payments:** **Cloud Spanner** (Global transactional consistency. No double-billing).
*   **Frontend:** **Global External Load Balancer** with Cloud CDN (Fast map loading).

## 2️⃣ Scenario B: The "Netflix" Clone 🎬
**Requirement:**
*   Petabytes of Video Content.
*   Global Distribution (Low Latency streaming).
*   Recommendation Engine (AI).

**The Solution:**
*   **Storage:** **Cloud Storage** (Archive/Standard class for video files).
*   **Distribution:** **Cloud CDN** (Cache video at the edge).
*   **Recommendations:** **BigQuery** (Store user watch history) -> **Vertex AI** (Train Model) -> **Cloud Run** (Serve predictions).

## 3️⃣ Scenario C: The "Bank" (Regulatory Heavy) 🏦
**Requirement:**
*   Strict Isolation (No internet access).
*   Audit Logs for 7 year retention.
*   Disaster Recovery (RPO < 15 mins).

**The Solution:**
*   **Network:** **Shared VPC** (Central IT control). No Public IPs. All traffic via **Cloud Interconnect** (Dedicated line to On-Prem).
*   **Security:** **VPC Service Controls** (Prevent data exfiltration). **CMEK** encryption.
*   **Database:** **Cloud SQL** (HA) with Cross-Region Replica (DR).
*   **Logging:** **Log Sink** -> **Cloud Storage (Archive Bucket)** with "Bucket Lock" (Compliance/WORM).

## 4️⃣ The "Decision Matrix" (Cheat Sheet) 🧠

| If you need... | Use... |
| :--- | :--- |
| **Global SQL** | Spanner |
| **Global NoSQL (High Write)** | Bigtable |
| **Serverless Containers** | Cloud Run |
| **Complex Orchestration** | GKE |
| **Event-Driven Snippet** | Cloud Functions |
| **Analytic Warehouse** | BigQuery |
| **Lift & Shift VM** | Compute Engine |

## 5️⃣ Checkpoint Questions (The Ultimate Test)
**Q1. A global retail company needs a database for their inventory. It must handle millions of updates per second (IoT sensors on shelves) and consistency is less important than speed. What do you choose?**
*   A. Cloud Spanner
*   B. Cloud SQL
*   C. Bigtable
*   D. BigQuery
> **Answer: C.** Bigtable is the king of write-heavy IoT throughput.

**Q2. You are designing a DR plan. You need an RPO (Recovery Point Objective) of near-zero. What strategy do you use?**
*   A. Nightly Backups.
*   B. Active-Passive Cold Standby.
*   C. **Synchronous Replication** (High Availability).
*   D. Tape drives.
> **Answer: C.** HA prevents data loss by writing to two zones simultaneously.

**Q3. Your compliance officer requires that no data ever traverses the public internet, even between Google services. What do you configure?**
*   A. Cloud VPN.
*   B. Private Google Access (PGA) & Private Service Connect.
*   C. HTTPS.
*   D. Cloud Armor.
> **Answer: B.** PGA allows VMs to reach Google APIs (Storage/BigQuery) via internal Google fiber.
