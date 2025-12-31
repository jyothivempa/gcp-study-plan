# SECTION 22: Cloud Spanner & Bigtable

> **Official Doc Reference**: [Spanner](https://cloud.google.com/spanner/docs) | [Bigtable](https://cloud.google.com/bigtable/docs)

## 1️⃣ Overview: The Heavy Hitters
*   **Cloud SQL** is great, but it hits a wall at ~10TB or ~50k TPS. It is also Regional.
*   **Cloud Spanner:** The "Impossible" Database.
    *   **Global Scale:** Replicated across US, Europe, Asia.
    *   **Strong Consistency:** If you write in Tokyo, NY sees it instantly. (Uses Atomic Clocks/TrueTime).
    *   **Relational:** Speaks SQL.
*   **Bigtable:** The "Fire Hose".
    *   **NoSQL:** Key-Value store. No complex queries (JOINs are hard).
    *   **Use Case:** IoT data, Stock Tickers, Ad Tech (Millions of writes/sec).

## 2️⃣ Comparison Table (Exam Gold 🥇)

| Feature | **Cloud SQL** | **Cloud Spanner** | **Bigtable** |
| :--- | :--- | :--- | :--- |
| **Type** | Relational (MySQL/Postgres) | Relational (SQL) | NoSQL (Wide Column) |
| **Scale** | Regional (Vertical Scale) | Global (Horizontal Scale) | Global (Horizontal Scale) |
| **Capacity** | ~10TB | Petabytes | Petabytes |
| **Consistency**| Strong | **Strong** (Global) | Eventual (Mostly) |
| **Best For** | CRM, ERP, Wordpress | Global Banking, Inventory | Time-series, IoT, Fintech |

## 3️⃣ Spanner Architecture (TrueTime) ⏰
How does Spanner guarantee consistency across the world?
*   **TrueTime API:** Google uses GPS and Atomic Clocks in every data center to sync time perfectly.
*   **Paxos:** The consensus algorithm used to agree on "Who wrote first?".

```mermaid
graph TD
    subgraph "TrueTime API (The 'God' Clock) ⏳"
        GPS[🛰️ GPS Satellites]
        Atomic[⚛️ Atomic Clocks]
    end

    subgraph "Spanner Instance (Multi-Region)"
        direction TB
        Leader[👑 US-Central (RW Leader)]
        Replica_EU[📖 Europe (Read-Only)]
        Witness[🗳️ US-East (Witness Node)]
        
        %% TrueTime Injection
        GPS -.->|Time Signal| Leader
        Atomic -.->|Time Signal| Leader
        GPS -.->|Time Signal| Replica_EU
        GPS -.->|Time Signal| Witness
    end

    %% Paxos & Replication Logic
    Leader --"Replication Log"--> Replica_EU
    Leader --"Paxos Vote"--> Witness
    Witness --"Paxos Ack"--> Leader

    classDef gold fill:#fffbeb,stroke:#b45309,stroke-width:2px;
    classDef green fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef grey fill:#f1f5f9,stroke:#64748b,stroke-dasharray: 5 5;

    class GPS,Atomic gold;
    class Leader green;
    class Witness grey;
```

## 4️⃣ Bigtable Schema Design (The "Hotspot" Trap) 🔥
Bigtable stores data alphabetically by **Row Key**.
*   **Bad Key:** `Timestamp` (e.g., `2025-01-01`).
    *   *Result:* All writes go to the *same* node (The end of the table). This is "Hotspotting".
*   **Good Key:** `ReverseTimestamp` or `DeviceID#Timestamp`.
    *   *Result:* Writes are spread evenly across all nodes.

## 5️⃣ Hands-On Lab: Create a Spanner Instance 🛠️
1.  **Create Instance:**
    ```bash
    gcloud spanner instances create my-bank \
        --config=regional-us-central1 \
        --description="Banking DB" \
        --nodes=1
    ```
2.  **Create Database:**
    ```bash
    gcloud spanner databases create transactions \
        --instance=my-bank
    ```
3.  **Run SQL:**
    ```bash
    gcloud spanner databases execute-sql transactions \
        --instance=my-bank \
        --sql="SELECT 1"
    ```

## 6️⃣ Exam Traps 🚨
*   **Trap:** "I need a global relational database, but Spanner is too expensive. Should I use Cloud SQL?"
    *   *Answer:* If you need **Global Writes**, you *must* use Spanner. Cloud SQL Read Replicas are global, but writes are single-region.
*   **Trap:** "I want to migrate my MongoDB to Bigtable."
    *   *Answer:* You *can*, but Bigtable is **Wide-Column** (HBase compatible), not Document-based. **Firestore** is usually the better Mongo alternative.
*   **Trap:** "Can I use JOINs in Bigtable?"
    *   *Answer:* No. Bigtable is NoSQL. You must Denormalize your data (duplicate it) to avoid joins.

## 7️⃣ Checkpoint Questions (Exam Style)
**Q1. Which GCP database service offers Strong Global Consistency using Atomic Clocks?**
*   A. Cloud SQL
*   B. Firestore
*   C. Cloud Spanner
*   D. Bigtable
> **Answer: C.** Spanner's TrueTime API is unique in the industry.

**Q2. Your Bigtable performance is slow. You look at the logs and see one node is at 100% CPU while others are at 5%. What is the problem?**
*   A. The cluster is too small.
*   B. You are experiencing **Hotspotting** due to a bad Row Key design.
*   C. The network bandwidth is saturated.
*   D. You need more HDD storage.
> **Answer: B.** Sequential keys (like timestamps) cause all traffic to hit one node.

**Q3. Which database is "Drop-in compatible" with the open-source Apache HBase API?**
*   A. BigQuery
*   B. Bigtable
*   C. Datastore
*   D. Spanner
> **Answer: B.** Bigtable *is* what Google built internally, which inspired HBase.
