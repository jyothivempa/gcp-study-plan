# SECTION 14: Logging & Monitoring (Cloud Operations)

## 1️⃣ Plain-English Explanation
*   **Logging:** The "Black Box" flight recorder. Records *events* (text). "Engine started." "Engine failed."
*   **Monitoring:** The Dashboard gauges. Records *health* (numbers). "Speed: 500mph", "Fuel: 90%".
*   **Trace:** The GPS. Tracks a single request as it jumps between services. "Latency maps".

## 2️⃣ Architecture Diagram: The Observability Pipeline

```mermaid
graph LR
    Source[VM / GKE / Database]
    
    subgraph "Cloud Logging"
        Ingest[Log Router]
        Bucket[Log Bucket: _Default]
        Sink[Log Sink]
    end
    
    subgraph "Destinations"
        Storage[Cloud Storage (Long Term Archive)]
        BigQuery[BigQuery (Analytics/SQL)]
        PubSub[Pub/Sub (Splunk/Datadog)]
    end
    
    Source --"Fluent Bit Agent"--> Ingest
    Ingest --> Bucket
    Ingest --"Filter: Error"--> Sink
    Sink --> Storage
    Sink --> BigQuery
    
    style Ingest fill:#e0f2fe,stroke:#0284c7
    style Sink fill:#fef3c7,stroke:#d97706
```
*   **Key Concept:** You don't have to keep logs in Cloud Logging (which is expensive). You can "Sink" them to Storage (Cheap) or BigQuery (Smart).

## 3️⃣ Metric Types (Exam Critical)
1.  **Gauge:** A value at a point in time. (e.g., "Temperature is 75°F"). Can go up or down.
2.  **Cumulative:** A value that only goes up. (e.g., "Total Miles Driven"). Can calculate rates.
3.  **Delta:** The change over a period. (e.g., "Miles driven in the last minute").

## 4️⃣ Zero-to-Hero: Uptime Checks & Alerting ⚡
**Scenario:** You want an SMS if your website (`www.example.com`) is down.
1.  **Uptime Check:** Google servers in Singapore, US, and Europe ping your URL every 1 minute.
2.  **Alerting Policy:**
    *   *Condition:* "Uptime Check Passed = False" for > 1 minute.
    *   *Notification Channel:* Email / SMS / PagerDuty.

## 5️⃣ Exam Scenarios & Traps 🚨
*   **Trap:** "I need to debug why a specific API call is taking 5 seconds. Metrics show CPU is low."
    *   *Answer:* Use **Cloud Trace**. Metrics (CPU) don't show latency bottlenecks between microservices. Trace visualizes the waterfall.
*   **Trap:** "I need to store Audit Logs for 7 years for legal compliance."
    *   *Answer:* Configure a **Log Sink** to **Cloud Storage (Archive Class)**. Do not keep them in Cloud Logging (Max retention is usually limited/expensive).
*   **Trap:** "I want to debug code running in production without stopping the server."
    *   *Answer:* **Cloud Snapshot Debugger** (Legacy) or "Source Context". (Though Debugger is deprecated, the concept remains: Non-breaking breakpoints).

## 6️⃣ Hands-On: Log-Based Metrics
**Power Move:** Turn Logs into Metrics.
*   *Use Case:* You have a legacy app that prints "Payment Failed" to the logs but doesn't emit a metric.
*   *Action:* Create a **Log-Based Metric**.
    *   *Filter:* `textPayload: "Payment Failed"`
    *   *Type:* Counter.
*   *Result:* Now you have a chart in Cloud Monitoring showing "Failed Payments per Second".

## 7️⃣ Checkpoint Questions (Exam Style)
**Q1. Which Cloud Operations tool is best for analyzing "Tail Latency" (e.g., the slowest 1% of requests)?**
*   A. Cloud Profiler
*   B. Cloud Trace
*   C. Cloud Logging
*   D. Cloud Monitoring
> **Answer: B.** Cloud Trace visualizes request latency across microservices.

**Q2. You need to export logs to a third-party SIEM tool (like Splunk). Which Sink Destination do you use?**
*   A. Cloud Storage
*   B. BigQuery
*   C. Pub/Sub
*   D. Cloud SQL
> **Answer: C.** Pub/Sub is the standard glue for streaming logs to external tools.

**Q3. What is the difference between a Gauge metric and a Cumulative metric?**
*   A. Gauge can go up/down (RAM usage); Cumulative only goes up (Total Requests).
*   B. Gauge is for text; Cumulative is for numbers.
*   C. Gauge is historical; Cumulative is real-time.
> **Answer: A.** Gauge = Speedometer. Cumulative = Odometer.
