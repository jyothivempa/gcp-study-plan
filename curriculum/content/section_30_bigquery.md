# SECTION 21: BigQuery (Data Warehouse)

> **Official Doc Reference**: [BigQuery Documentation](https://cloud.google.com/bigquery/docs)

## 1️⃣ Overview: serverless Analytics
*   **What is it?** A Petabyte-scale Data Warehouse.
*   **The Magic:** You can query 1 TB of data in seconds using standard SQL.
*   **Serverless:** No provisioning. No disks to manage. Just upload data and run `SELECT *`.

## 2️⃣ Architecture: Separation of Storage & Compute
BigQuery is two services in a trench coat.
1.  **Colossus (Storage):** Cheap. Stores data in a columnar format (Capacitor).
2.  **Dremel (Compute):** Fast. Thousands of servers connect to storage, process the query, and vanish.
*   **Benefit:** You pay for storage (cheap) separately from analysis (queries).

## 3️⃣ Cost Model: Slots vs On-Demand 💰
How do you pay?

| Model | Pricing | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **On-Demand** | **$5 per TB** scanned. | Pay only for what you run. Easy. | Can get expensive if you run `SELECT *` on huge tables. |
| **Capacity (Slots)** | **Fixed $/hour** (e.g. $1000/mo). | Predictable bill. No surprises. | You pay even if you don't run queries. |

## 4️⃣ Zero-to-Hero: Partitioning & Clustering ⚡
*   **The Problem:** Scanning a full table costs money ($5/TB).
*   **Solution 1: Partitioning:** Divide the table by **Date**.
    *   *Query:* `WHERE date = '2025-01-01'`.
    *   *Effect:* BQ only scans that one day's file. Massive savings.
*   **Solution 2: Clustering:** Sort the data inside the partition (e.g., by `CustomerID`).
    *   *Effect:* Faster lookups for specific customers.

## 5️⃣ Hands-On Lab: Public Datasets 📊
You don't need your own data. BigQuery hosts public data (Covid, Weather, GitHub).
1.  **Open:** BigQuery Console.
2.  **Add Data:** Public Datasets > "USA Names".
3.  **Run Query:**
    ```sql
    SELECT name, sum(number) as total
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE name = 'Alice'
    GROUP BY name
    ```
4.  **Result:** 200ms duration. 10MB processed. Cost: $0.00.

## 6️⃣ Exam Traps 🚨
*   **Trap:** "I want to save money on queries. Should I use `LIMIT 10`?"
    *   *Answer:* **NO!** `LIMIT` only affects the output *after* scanning the full table. BigQuery charges for bytes *scanned*. Use **Partition filters** (`WHERE date=...`) to verify cost.
*   **Trap:** "I need real-time data streaming into BigQuery."
    *   *Answer:* Use the **Streaming API** (insertAll). Note: It costs extra money per GB inserted, unlike batch loading (which is free).

## 7️⃣ Checkpoint Questions (Exam Style)
<!--
**Q1. You accidentally run `SELECT *` on a Petabyte table. What happens?**
*   A. The query fails.
*   B. You get a bill for $5,000.
*   C. Google warns you first.
*   D. Nothing, it's free.
> **Answer: B.** BigQuery charges per Byte Scanned. Always check the "This query will process X GB" validator before running!

**Q2. Which optimization technique divides a table into segments based on a timestamp column?**
*   A. Sharding
*   B. Clustering
*   C. Partitioning
*   D. Indexing
> **Answer: C.** Partitioning enables "Pruning" (skipping irrelevant files).

**Q3. Is BigQuery a relational database (OLTP) replacement for Cloud SQL?**
*   A. Yes, it supports SQL.
*   B. No, it is a Columnar OLAP warehouse (bad for small frequent updates).
> **Answer: B.** Use Cloud SQL for transactions (Buying a ticket). Use BigQuery for analytics (Counting how many tickets sold last year).
-->
