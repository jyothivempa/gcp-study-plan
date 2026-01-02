# SECTION 24: Cloud Functions & Eventarc

## 1️⃣ Cloud Functions (Gen 2)
*   **FaaS (Function as a Service):** Upload Python/NodeJS code. Google runs it.
*   **Trigger types:**
    *   **HTTP:** Webhook.
    *   **Background (Eventarc):** "File uploaded to GCS", "Pub/Sub message received".

## 2️⃣ Eventarc
*   The glue between services.
*   **Standardized:** Uses CloudEvents format.
*   **Example:** User uploads image -> Eventarc detects -> Triggers Function -> Resizes image.

## 7️⃣ Checkpoint Questions
1.  **Cloud Functions Gen 2 is built on top of which service?**
    *   *Answer: Cloud Run.*
