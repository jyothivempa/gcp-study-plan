# SECTION 11: Cloud NAT & Routes

## 1️⃣ Plain-English Explanation: "The One-Way Mirror"
Imagine your private database servers are in a secure room (Private Subnet).
*   **The Rule:** NOBODY can enter the room (No Public IP).
*   **The Problem:** The servers need to download software updates from the internet.
*   **The Solution:** You install a **Cloud NAT** (Network Address Translation) gateway. It's like a one-way mirror. The servers can look out (send requests), but the internet cannot look in (initiate connections).

## 2️⃣ Architecture Diagram

```mermaid
graph LR
    subgraph "GCP VPC"
        VM[Private VM (No Public IP)] -- "1. Request Update" --> Router[Cloud Router]
        Router -- "2. NAT Translation" --> NAT[Cloud NAT Gateway]
    end
    
    NAT -- "3. Public IP Request" --> Internet((Internet / Repo))
    Internet -- "4. Reply" --> NAT
    NAT -- "5. Forward Reply" --> VM
    
    Hacker((Hacker)) --X "6. SSH Attack (Blocked)" --> NAT
    
    style NAT fill:#fce8e6,stroke:#ea4335,stroke-width:2px
    style Router fill:#fef3c7,stroke:#d97706
```

## 3️⃣ Why use Cloud NAT?
1.  **Security**: Reduces the attack surface. 0 Public IPs on your database = 0 Open Ports available to scanners.
2.  **Availability**: It is a regional managed service. High Availability is built-in.
3.  **Cost**: You pay per gateway uptime + data processing.

## 4️⃣ Routing Basics (The GPS)
A **Route** tells a packet where to go next ("Next Hop").
*   **Default Route (`0.0.0.0/0`):** "If you don't know where to go, go to the Internet Gateway."
*   **Subnet Route (`10.0.0.0/9`):** "If looking for `10.x.x.x`, stay inside the VPC."
*   **Static Route:** You manually create a route (e.g. "Send traffic for `192.168.1.5` to my VPN Gateway").

## 5️⃣ Cloud Router (The Brain 🧠)
Cloud NAT is effectively "powered by" **Cloud Router**.
*   **Cloud Router** is a control-plane device (it doesn't touch the packets effectively, it manages the rules).
*   It speaks **BGP** (Border Gateway Protocol) to dynamically learn routes from your On-Prem VPN.

## 6️⃣ Hands-On: Console Walkthrough
1.  **Go to:** Network Services > Cloud NAT.
2.  **Click:** Get Started.
3.  **Create:** Cloud Router (Required).
4.  **Name:** `nat-gateway-us`.
5.  **Region:** `us-central1` (NAT IS REGIONAL!).
6.  **NAT Mapping:** "Automatic (ALL Subnets)".
7.  **Test:**
    *   Create a VM with "Public IP: None".
    *   SSH into it (via IAP).
    *   Run `curl google.com`.
    *   **Success:** It works!

## 7️⃣ Exam Traps 🚨
*   **Trap:** "I used Cloud NAT, so now I can SSH into my VM from my laptop."
    *   *Answer:* **FALSE.** Cloud NAT is Outbound ONLY. To SSH in, you need **Identity-Aware Proxy (IAP)** or a Bastion Host.
*   **Trap:** "Is Cloud NAT a global resource?"
    *   *Answer:* **No.** It is Regional. If you have subnets in US and Europe, you need 2 NAT Gateways.
*   **Trap:** "My NAT is dropping packets."
    *   *Answer:* Check the **Port Usage**. If thousands of VMs share one IP, you might run out of ephemeral ports. Increase the number of NAT IPs.

## 8️⃣ Checkpoint Questions
**Q1. True or False: Cloud NAT allows a private VM to serve a public website.**
*   A. True
*   B. False
> **Answer: B.** False. NAT is for outbound traffic. To serve a website (Inbound), you need a Load Balancer with a Public IP.

**Q2. Which GCP component is required to configure Cloud NAT?**
*   A. Cloud Armor
*   B. Cloud Router
*   C. Cloud VPN
*   D. VPC Peering
> **Answer: B.** Cloud Router holds the configuration for Cloud NAT.

**Q3. If a packet matches two routes, which one does GCP pick?**
*   A. The one with the highest priority number.
*   B. The most specific destination range (Longest Prefix Match).
*   C. The oldest route.
*   D. Randomly.
> **Answer: B.** Standard networking logic: Longest Prefix Match wins (e.g., `/24` wins over `/16`). If prefixes match, then Priority wins.

**Q4. You need to connect your VPC to your On-Premises datacenter using dynamic routing. What protocol do you use?**
*   A. OSPF
*   B. RIP
*   C. BGP (Border Gateway Protocol)
*   D. ICMP
> **Answer: C.** Cloud Router uses BGP to exchange routes dynamically.


<!-- FLASHCARDS
[
  {
    "term": "Cloud NAT",
    "def": "Allows private VMs to access the internet for updates without a public IP."
  },
  {
    "term": "Route",
    "def": "Rules telling traffic where to go (Next Hop)."
  },
  {
    "term": "Dynamic Routing",
    "def": "Uses Cloud Router & BGP to automatically learn routes."
  },
  {
    "term": "System Routes",
    "def": "Default routes Google creates (e.g., Default Internet Gateway)."
  },
  {
    "term": "Bastion Host",
    "def": "Jump server used to SSH into private VMs securely."
  }
]
-->
