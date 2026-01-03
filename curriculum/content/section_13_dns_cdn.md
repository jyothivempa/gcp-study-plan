# SECTION 13: Cloud DNS & Cloud CDN

## 1️⃣ Plain-English Explanation
*   **Cloud DNS:** It's the "Phonebook" of the internet. It translates "google.com" to "142.250.x.x". In GCP, it's 100% SLA (never goes down).
*   **Cloud CDN (Content Delivery Network):** It's like having a mini-store in every city. Instead of fetching images from your warehouse in New York every time, you store copies (cache) in London, Tokyo, and Mumbai. Users download fast.

## 2️⃣ Cloud DNS Key Concepts
*   **Managed Zones:** Where you store your records (A, CNAME, TXT).
*   **Public Zones:** Visible to internet.
*   **Private Zones:** Only visible to your VPC. Used for internal services (e.g., `db.internal.corp`).
*   **Split Horizon:** Using the *same* domain name (myapp.com) but returning a private IP for internal users and public IP for external users.

## 3️⃣ Cloud CDN
*   **Works with:** Global HTTP(S) Load Balancer.
*   **Cache Hit:** Content served from edge (Fast!).
*   **Cache Miss:** Content fetched from backend (Slower).
*   **Invalidation:** Manually clearing the cache (e.g., you updated `logo.png` but users still see old one).



## 4️⃣ Exam Scenarios & Traps 🚨
*   **Trap:** "Users are complaining about stale content." -> **Invalidate the cache.**
*   **Trap:** "Need internal DNS names for VMs." -> **Private Managed Zone.**
*   **Trap:** "100% Availability for DNS." -> **Cloud DNS** is the only service with 100% SLA.

## 7️⃣ Checkpoint Questions
1.  **True or False: Cloud CDN can be used with a Regional Load Balancer.**
    *   *Answer: False. Requires Global HTTP(S) Load Balancer.*
2.  **Which DNS record type points a domain to an IP address?**
    *   *Answer: A Record.*
