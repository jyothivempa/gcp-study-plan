# SECTION 18: Cloud Run (Serverless Containers)

> **Official Doc Reference**: [Cloud Run Documentation](https://cloud.google.com/run/docs)

## 1️⃣ Overview: The "Pop-up Food Truck"
*   **Concept:** You give Google a **Container Image**. Google runs it only when a request comes in.
*   **The Killer Feature:** **Scale to Zero**. If nobody visits your site at 3 AM, you pay $0.00.
*   **Concurrency:** Unlike AWS Lambda (1 request per instance), Cloud Run can handle **80 (defaults) to 1000** requests per container. This saves massive money.

## 2️⃣ Architecture Diagram

```mermaid
graph LR
    User --> HTTPS[HTTPS Endpoint]
    HTTPS --> Scaling{Traffic?}
    
    Scaling --"0 Requests"--> Zero[0 Containers ($0 Cost)]
    Scaling --"100 Requests"--> Container1[Container A (80 req)]
    Scaling --"Overflow"--> Container2[Container B (20 req)]
    
    style Zero fill:#f3f4f6,stroke:#9ca3af,stroke-dasharray: 5 5
    style Container1 fill:#dcfce7,stroke:#15803d
    style Container2 fill:#dcfce7,stroke:#15803d
```

## 3️⃣ Cloud Run vs App Engine vs Functions

| Feature | **Cloud Run** | **Cloud Functions** | **App Engine** |
| :--- | :--- | :--- | :--- |
| **Unit of Code** | **Container** (Any Language/Binary) | **Function** (Snippet) | **App** (Web Server) |
| **Portability** | **High** (Run anywhere with Docker) | **Low** (GCP Specific) | **Medium** |
| **Language** | Anything (Rust, C++, Fortran) | Python, Node, Go, Java | Python, Node, Go, Java |
| **Best For** | REST APIs, Microservices, Websites | Event Triggers (File Uploaded) | Legacy Monoliths |

## 4️⃣ Hands-On Lab: Deploy a Container 🐋
1.  **Enable API:**
    `gcloud services enable run.googleapis.com`
2.  **Deploy (From Google's Sample Image):**
    ```bash
    gcloud run deploy my-service \
        --image=us-docker.pkg.dev/cloudrun/container/hello \
        --allow-unauthenticated \
        --region=us-central1
    ```
3.  **Result:** You get a `https://my-service-xyz.run.app` URL instantly. SSL is included.

## 5️⃣ Zero-to-Hero: Jobs vs Services ⚡
*   **Cloud Run Services:** Good for HTTP requests (Website, API). Runs as long as the request lasts.
*   **Cloud Run Jobs:** Good for batch work (Image processing, Database migration). Runs until the task is "Done".

## 6️⃣ Exam Traps 🚨
*   **Trap:** "I have a WebSocket application (Chat App). Can I use Cloud Run?"
    *   *Answer:* **Yes.** Cloud Run supports WebSockets and HTTP/2 and gRPC.
*   **Trap:** "I need to mount a file system (NFS) to my container."
    *   *Answer:* You can mount **Cloud Storage FUSE** or **Memorystore**, or use the new **Network File System (NFS)** volume execution environment (Gen 2).
*   **Trap:** "My container takes 5 minutes to start up. Why does the request fail?"
    *   *Answer:* Cloud Run expects fast startup. If you need long startup, configure **min-instances** (so it stays warm).

## 7️⃣ Checkpoint Questions (Exam Style)
**Q1. What is the default pricing model for Cloud Run when no requests are coming in?**
*   A. You pay for 1 idle instance.
*   B. You pay for the load balancer only.
*   C. You pay **$0**.
*   D. You pay a reservation fee.
> **Answer: C.** Scale to Zero means Zero cost.

**Q2. Unlike AWS Lambda, a single Cloud Run instance can handle:**
*   A. Only 1 request at a time.
*   B. Multiple concurrent requests (Concurrency).
*   C. Only UDP traffic.
*   D. Only internal traffic.
> **Answer: B.** Default concurrency is 80. This makes it much cheaper for high-volume APIs.

**Q3. To allow public internet access to your Cloud Run service, you must use which flag?**
*   A. `--make-public`
*   B. `--allow-unauthenticated`
*   C. `--public-access`
*   D. `--internet-gateway`
> **Answer: B.** By default, Cloud Run is private (IAM protected). You must explicitly allow unauthenticated access.
