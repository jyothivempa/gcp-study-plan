# SECTION 34: Data Capstone (The Slow Report)

## 🕵️‍♂️ The Scenario
The Marketing Director is angry.
The "Daily Sales Report" dashboard used to load in 5 seconds.
Now it takes **5 minutes** and costs **$50 per run**.
The dataset has grown to 10 TB.

## 1️⃣ The "Bad" Query
```sql
SELECT * 
FROM `sales.transactions_all`
WHERE transaction_date = '2025-01-01'
ORDER BY customer_id
```
*   **The Problem:** `SELECT *` scans ALL columns. The table is NOT partitioned. It scans the full 10 TB history just to find one day.

## 2️⃣ The Objectives
1.  **Analyze:** Use `bq query --dry_run` to see the cost.
2.  **Optimize:** Create a **Partitioned Table**.
3.  **Verify:** Reduce the scan size from 10 TB to 10 GB (1000x cheaper).

## 3️⃣ Lab Steps (Guided) 🛠️

### Step 1: The Diagnosis
Running the bad query:
*   "This query will process 10.24 TB." -> Cost: ~$50.

### Step 2: The Fix (Partitioning)
Create a new table partitioned by date.
```sql
CREATE TABLE `sales.transactions_optimized`
PARTITION BY DATE(transaction_date)
AS
SELECT * FROM `sales.transactions_all`
```
*   *Note:* This takes time to run once, but future queries are fast.

### Step 3: The Fix (Clustering) - Bonus
Cluster by `customer_id` for faster sorting.
```sql
CREATE TABLE `sales.transactions_optimized_clustered`
PARTITION BY DATE(transaction_date)
CLUSTER BY customer_id
AS ...
```

### Step 4: The Validation 📉
Run the specific query on the new table:
```sql
SELECT * 
FROM `sales.transactions_optimized`
WHERE transaction_date = '2025-01-01'
```
*   *Result:* "This query will process 10 GB." -> Cost: $0.05.

## 4️⃣ Checkpoint Questions
**Q1. Why is `SELECT *` considered a BigQuery anti-pattern?**
*   A. It looks ugly.
*   B. It returns too many rows.
*   C. It scans every column, maximizing the cost (which uses Columnar storage).
*   D. It deletes data.
> **Answer: C.** BigQuery is Columnar. Reading one column is cheap. Reading all columns is expensive.

**Q2. Partitioning a table by Date allows the query engine to:**
*   A. Compress the data better.
*   B. **Prune** (skip) files that don't match the date filter.
*   C. Delete old data automatically.
*   D. Encrypt the data.
> **Answer: B.** Partition Pruning is the #1 cost saver.

**Q3. If you frequently filter by `User_ID` *within* a specific Date, what should you add?**
*   A. An Index.
*   B. A Foreign Key.
*   C. **Clustering** on `User_ID`.
*   D. Nothing.
> **Answer: C.** Clustering sorts data inside the partition, making lookups faster.
