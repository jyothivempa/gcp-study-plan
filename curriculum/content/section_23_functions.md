# SECTION 23: Cloud Functions & Eventarc

> **Official Doc Reference**: [Cloud Functions](https://cloud.google.com/functions/docs)

## 1️⃣ Overview: The "Glue" of the Cloud
*   **Concept:** "I don't want a server. I don't even want a container. I just want this Python script to run when a file is uploaded."
*   **Function as a Service (FaaS):** Single purpose, event-driven, short-lived (max 60 mins).

## 2️⃣ Architecture Diagram: Event-Driven Logic

```mermaid
graph LR
    User[User] --"Uploads Image"--> Bucket[Cloud Storage]
    Bucket --"Event Trigger (Finalize)"--> Eventarc[Eventarc Bus]
    Eventarc --"Push"--> Function[Cloud Function (Resize Image)]
    Function --"Save Thumbnail"--> Bucket
    
    style Function fill:#dcfce7,stroke:#15803d
    style Eventarc fill:#fef3c7,stroke:#d97706
```

## 3️⃣ Gen 1 vs Gen 2 (Exam Critical)
Google upgraded Cloud Functions recently.

| Feature | **Gen 1** | **Gen 2 (The Standard)** |
| :--- | :--- | :--- |
| **Underlying Tech** | Proprietary Google | **Cloud Run** (Knative) |
| **Concurrency** | 1 Request per Instance | **1000 Requests** per Instance (Save $$$) |
| **Execution Time** | Max 9 mins | Max 60 mins |
| **Triggers** | Background Functions | **Eventarc** (Standardized CloudEvents) |

## 4️⃣ Zero-to-Hero: Idempotency ⚡
*   **The Problem:** Events are "At-Least-Once" delivery. Your function might run **twice** for the same file upload.
*   **The Fix:** Make your code **Idempotent**.
    *   *Bad:* `counter = counter + 1` (Result: 2).
    *   *Good:* `if not exists(file): create(file)` (Result: 1).

## 5️⃣ Hands-On Lab: The Storage Trigger 📸
1.  **Create Bucket:** `gs://input-bucket`.
2.  **Deploy Function:**
    ```bash
    gcloud functions deploy verify-file \
        --gen2 \
        --runtime=python310 \
        --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
        --trigger-event-filters="bucket=input-bucket" \
        --entry-point=verify_file_handler
    ```
3.  **Test:** Upload a file. Check Function logs.

## 6️⃣ Exam Traps 🚨
*   **Trap:** "I need to run a batch job that takes 4 hours."
    *   *Answer:* Do **NOT** use Cloud Functions (Max 60 mins). Use **Cloud Run Jobs** or **Batch**.
*   **Trap:** "I want to prevent my function from scaling to infinity and costing $10,000."
    *   *Answer:* Set `--max-instances`. This acts as a "Budget Cap" (but will drop traffic if exceeded).
*   **Trap:** "How do I connect a Function to a VPC Database?"
    *   *Answer:* Use a **VPC Connector** (Serverless VPC Access). Functions are outside the VPC by default.

## 7️⃣ Checkpoint Questions (Exam Style)
**Q1. Which Cloud Function generation allows for concurrent request processing (up to 1000)?**
*   A. Gen 1
*   B. Gen 2
*   C. Both
*   D. Neither (Use Cloud Run)
> **Answer: B.** Gen 2 is built on top of Cloud Run, inheriting its concurrency benefits.

**Q2. What is the maximum execution timeout for a Gen 2 Cloud Function?**
*   A. 9 minutes
*   B. 15 minutes
*   C. 60 minutes
*   D. 24 hours
> **Answer: C.** Greatly expanded from Gen 1.

**Q3. Your function writes a "Welcome" email when a user signs up. Users are complaining they received the email twice. What logic is missing?**
*   A. Authentication
*   B. Idempotency
*   C. Authorization
*   D. Encryption
> **Answer: B.** You must handle duplicate events gracefully.
