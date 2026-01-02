# SECTION 23: Cloud Functions & Eventarc (Event-Driven)

> **Official Doc Reference**: [Cloud Functions](https://cloud.google.com/functions/docs) | [Eventarc](https://cloud.google.com/eventarc/docs)

## 1️⃣ What is "Event-Driven"?
Imagine a **Rube Goldberg machine**.
*   **Trigger:** User uploads an image to Cloud Storage.
*   **Action:** Cloud Function wakes up, resizes the image, and shuts down.
*   **Result:** You pay for 200ms of compute.

**Cloud Functions (2nd Gen)** build on Cloud Run technology but hide the container complexity. You just write code (Python, Go, Node.js).

## 2️⃣ Cloud Functions 2nd Gen vs 1st Gen

| Feature | 1st Gen | 2nd Gen (Preferred) |
| :--- | :--- | :--- |
| **Infrastructure** | Proprietary | **Cloud Run** (Portable) |
| **Request Timeout** | 9 mins | **60 mins** (HTTP) |
| **Concurrency** | 1 req / instance | **1000 reqs / instance** (Cheaper) |
| **Triggers** | Pub/Sub, Storage | **Eventarc** (100+ triggers) |

## 3️⃣ Eventarc: The Glue
Eventarc lets you listen to almost *any* Google Cloud event (Audit Logs).
*   *e.g., "Trigger function when a BigQuery Job finishes."*
*   *e.g., "Trigger function when a VM is created."*

## 4️⃣ Hands-On Lab: The "Thumbnail Generator" 🖼️

**Scenario:** We want to log a message every time a file is uploaded to a specific bucket.

### Step 1: Create the Bucket
```bash
export BUCKET_NAME="monitor-me-${PROJECT_ID}"
gcloud storage buckets create gs://$BUCKET_NAME --location=us-central1
```

### Step 2: Write the Code (main.py)
```python
import functions_framework

@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data
    event_id = cloud_event["id"]
    event_type = cloud_event["type"]
    bucket = data["bucket"]
    name = data["name"]

    print(f"Event ID: {event_id}")
    print(f"Event Type: {event_type}")
    print(f"File: {name} uploaded to {bucket}")
```

### Step 3: Deploy Function (2nd Gen)
```bash
gcloud functions deploy file-monitor \
    --gen2 \
    --runtime=python310 \
    --region=us-central1 \
    --source=. \
    --entry-point=hello_gcs \
    --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
    --trigger-event-filters="bucket=$BUCKET_NAME"
```
*(Deploying takes ~2 mins)*

### Step 4: Test It
1.  Upload a file:
    ```bash
    echo "Test File" > test.txt
    gcloud storage cp test.txt gs://$BUCKET_NAME
    ```
2.  Check Logs:
    ```bash
    gcloud functions logs read file-monitor --region=us-central1 --limit=5
    ```
3.  **Success:** You should see "File: test.txt uploaded..."

## 5️⃣ Exam Tips 💡
1.  **" glue code"** = Cloud Functions.
2.  **"Long running process (>9 mins)"** = Cloud Run or Batch (NOT Functions 1st gen).
3.  **"Trigger on Cloud Storage upload"** = Eventarc or Background Trigger.
4.  **"Keep warm"** = Set `--min-instances 1` to avoid cold starts.

## 6️⃣ Checkpoint Questions

**Q1. You need to process a file uploaded to GCS. The processing takes 45 minutes. Which service do you choose?**
*   A. Cloud Functions 1st Gen
*   B. **Cloud Functions 2nd Gen** (or Cloud Run)
*   C. App Engine Standard
> **Answer: B.** 2nd Gen supports up to 60 min timeouts. 1st Gen is hard-capped at 9 mins.

**Q2. Which tool allows you to trigger a function from *any* Cloud Audit Log?**
*   A. Cloud Scheduler
*   B. **Eventarc**
*   C. Pub/Sub
> **Answer: B.** Eventarc unifies eventing across GCP.

## ✅ Day 23 Checklist
<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I understand the difference between 1st and 2nd Gen functions.', checked: false },
        { text: 'I deployed a function triggered by Cloud Storage.', checked: false },
        { text: 'I know what Eventarc is.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 23 Checklist
    </h3>
    <template x-for="(item, index) in items" :key="index">
        <div class="checklist-item" @click="item.checked = !item.checked">
            <div class="checklist-box" :class="{ 'checked': item.checked }">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
            </div>
            <span x-text="item.text" :class="{ 'line-through text-slate-400': item.checked }"></span>
        </div>
    </template>
</div>
