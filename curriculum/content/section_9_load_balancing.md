# Day 9: Cloud Load Balancing & CDN

**Duration:** ⏱️ 60 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐⭐ Critical (Load Balancing is heavily tested)

---

## 🎯 Learning Objectives

By the end of Day 9, you will be able to:

*   **Understand** Layer 4 vs Layer 7 load balancing
*   **Explain** how Anycast IPs provide global routing
*   **Choose** the right load balancer for each scenario
*   **Configure** Cloud CDN for content caching
*   **Implement** SSL termination and health checks

---

## 🧠 1. Why Load Balancing? (Plain-English)

**Problem:** You have 10,000 users but only 1 web server → it crashes.  
**Solution:** Use 10 servers and a Load Balancer to distribute traffic.

### 💡 Real-World Analogy: Airport Check-In

| LB Concept | Airport Analogy |
|------------|-----------------|
| **Load Balancer** | Check-in counter manager |
| **Backend Servers** | Individual check-in counters |
| **Health Check** | "Counter Open/Closed" sign |
| **Anycast IP** | Single airport entrance that routes to nearest terminal |

---

## 🏗️ 2. GCP Load Balancer Types

### The "ACE Master" Decision Tree

```mermaid
flowchart TD
    Start([Need Load Balancing?]) --> Traffic{Traffic Type?}
    Traffic -- HTTP/HTTPS --> L7[Layer 7: Application LB]
    Traffic -- TCP/UDP/SSL --> L4[Layer 4: Network LB]

    L7 --> L7Scope{Scope?}
    L7Scope -- Global --> G7[Global External HTTP/S LB]
    L7Scope -- Regional --> R7[Regional External HTTP/S LB]
    L7Scope -- Private --> I7[Internal HTTP/S LB]

    L4 --> L4Ext{External?}
    L4Ext -- Yes --> L4Proxy{Proxy or Pass thru?}
    L4Proxy -- Proxy / Anycast --> G4[Global External Proxy LB]
    L4Proxy -- Pass through --> RN4[Regional Network LB]
    L4Ext -- No --> I4[Internal TCP/UDP LB]

    style G7 fill:#dcfce7,stroke:#16a34a,stroke-width:2px
    style G4 fill:#dcfce7,stroke:#16a34a,stroke-width:2px
    style Start fill:#f1f5f9
```

### Complete LB Comparison

| Load Balancer | Layer | Scope | Use Case |
|--------------|-------|-------|----------|
| **Global External HTTP(S)** | L7 | Global | Web apps, APIs, mobile backends |
| **Global External TCP/SSL** | L4 | Global | Non-HTTP TCP (gaming, IoT) |
| **Regional External HTTP(S)** | L7 | Regional | Compliance (data must stay in region) |
| **Regional External Network** | L4 | Regional | UDP, non-HTTP protocols |
| **Internal HTTP(S)** | L7 | Regional | Private microservices |
| **Internal TCP/UDP** | L4 | Regional | Internal databases, apps |

> **🎯 ACE Tip:** If the question says "global" and "web app" → **Global HTTP(S) LB**. If it says "gaming" or "UDP" → **Network LB**.

---

## 🌍 3. Anycast IP: The Magic of Global Load Balancing

### How Anycast Works

```mermaid
sequenceDiagram
    participant US as User (US)
    participant EU as User (EU)
    participant IP as Single Anycast IP
    participant GLB as Global LB
    participant MUS as MIG (US)
    participant MEU as MIG (EU)
    
    US->>IP: Request
    IP->>GLB: Routes to nearest
    GLB->>MUS: Forward to US backend
    
    EU->>IP: Request (same IP!)
    IP->>GLB: Routes to nearest
    GLB->>MEU: Forward to EU backend
```

**Key Benefits:**
*   Single IP address for global reach
*   Automatic routing to nearest healthy backend
*   No DNS changes needed for failover

---

## 🔒 4. SSL Termination & Certificates

### SSL Offloading Architecture

```mermaid
flowchart LR
    subgraph Internet
        U[User]
    end
    
    subgraph Edge["Google Edge"]
        LB[Load Balancer<br/>SSL Termination]
    end
    
    subgraph Backend
        VM1[VM 1]
        VM2[VM 2]
    end
    
    U -->|HTTPS encrypted| LB
    LB -->|HTTP unencrypted| VM1 & VM2
    
    style LB fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
```

**Benefits:**
*   Offload CPU-intensive SSL from backend VMs
*   Centralized certificate management
*   Use Google-managed certificates (auto-renewing)

---

---

## 🛡️ 6. Cloud Armor: The Bodyguard
When using the **Global HTTP(S) Load Balancer**, you can enable **Cloud Armor**.

*   **DDoS Protection:** Blocks volumetric attacks at the edge.
*   **WAF (Web Application Firewall):** Blocks common attacks like SQL Injection (SQLi) and Cross-Site Scripting (XSS).
*   **IP Whitelisting/Blacklisting:** Allow or block specific CIDR ranges.

> [!IMPORTANT]
> **ACE Tip:** Cloud Armor only works with **External HTTP(S) Load Balancers**. It cannot be used directly on VMs or Internal LBs.

---

## 🛠️ 6. Hands-On Lab: Create Global HTTP(S) LB

### Step 1: Create Instance Template
```bash
gcloud compute instance-templates create web-template \
    --machine-type=e2-micro \
    --tags=http-server \
    --metadata=startup-script='#!/bin/bash
apt-get update && apt-get install -y nginx
echo "<h1>Hello from $(hostname)</h1>" > /var/www/html/index.html'
```

### Step 2: Create Managed Instance Groups
```bash
# US region
gcloud compute instance-groups managed create mig-us \
    --template=web-template \
    --size=2 \
    --zone=us-central1-a

# EU region  
gcloud compute instance-groups managed create mig-eu \
    --template=web-template \
    --size=2 \
    --zone=europe-west1-b
```

### Step 3: Create Health Check
```bash
gcloud compute health-checks create http http-health-check \
    --port=80 \
    --request-path=/
```

### Step 4: Create Backend Service
```bash
gcloud compute backend-services create web-backend \
    --protocol=HTTP \
    --health-checks=http-health-check \
    --global

gcloud compute backend-services add-backend web-backend \
    --instance-group=mig-us \
    --instance-group-zone=us-central1-a \
    --global

gcloud compute backend-services add-backend web-backend \
    --instance-group=mig-eu \
    --instance-group-zone=europe-west1-b \
    --global
```

### Step 5: Create URL Map and Frontend
```bash
# URL map
gcloud compute url-maps create web-map \
    --default-service=web-backend

# HTTP proxy
gcloud compute target-http-proxies create http-proxy \
    --url-map=web-map

# Global forwarding rule (gets Anycast IP)
gcloud compute forwarding-rules create http-rule \
    --global \
    --target-http-proxy=http-proxy \
    --ports=80
```

### Step 6: Test
```bash
# Get the external IP
gcloud compute forwarding-rules describe http-rule --global --format="value(IPAddress)"

# Wait 5-10 minutes for propagation, then curl
curl http://YOUR_IP
```

---

## ⚠️ 7. Exam Traps & Pro Tips

### ❌ Common Mistakes
| Mistake | Reality |
|---------|---------|
| "Network LB is for web apps" | No! Network LB is for non-HTTP (Layer 4) |
| "Health checks are optional" | No! LB can't function properly without them |
| "LB starts working immediately" | No! Global LB takes 5-10 minutes |

### ✅ Pro Tips
*   **Use Google-managed SSL certificates** - auto-renewing, free
*   **Enable Cloud CDN** on static content for 50-90% latency reduction
*   **Use named ports** in instance groups for flexibility
*   **Set appropriate health check intervals** (not too aggressive)

---

<!-- QUIZ_START -->
## 📝 8. Knowledge Check Quiz

1. **Which Load Balancer would you use for a global mobile app with a single IP address?**
    *   A. Regional Network LB
    *   B. **Global External HTTP(S) LB** ✅
    *   C. Internal TCP LB
    *   D. Regional HTTP(S) LB

2. **At which OSI layer does a Network Load Balancer operate?**
    *   A. Layer 7 (Application)
    *   B. **Layer 4 (Transport)** ✅
    *   C. Layer 3 (Network)
    *   D. Layer 2 (Data Link)

3. **What does SSL termination at the Load Balancer provide?**
    *   A. End-to-end encryption
    *   B. **Offloads SSL decryption from backend VMs** ✅
    *   C. Automatic firewall rules
    *   D. DDoS protection only

4. **You need to cache static images globally to reduce latency. What should you enable?**
    *   A. VPC Peering
    *   B. Cloud Armor
    *   C. **Cloud CDN** ✅
    *   D. Cloud NAT

5. **How long should you wait for a Global HTTP(S) LB to start working after creation?**
    *   A. Instant
    *   B. 1 minute
    *   C. **5-10 minutes** ✅
    *   D. 1 hour
<!-- QUIZ_END -->

---

## ✅ Day 9 Checklist

- [ ] Understand Layer 4 vs Layer 7 differences
- [ ] Know which LB type for each scenario
- [ ] Configure health checks
- [ ] Set up Cloud CDN for caching
- [ ] Complete the hands-on lab

---

<!-- FLASHCARDS
[
  {"term": "Anycast IP", "def": "Single IP that routes users to the nearest Google edge location automatically."},
  {"term": "Layer 7 LB", "def": "Application layer. Can inspect HTTP headers, URLs, cookies for routing."},
  {"term": "Layer 4 LB", "def": "Transport layer. Routes based on IP/port only. For TCP/UDP."},
  {"term": "Health Check", "def": "Periodic probe to verify backend is healthy. Unhealthy = no traffic."},
  {"term": "SSL Termination", "def": "Decrypting HTTPS at the LB, sending HTTP to backends. Reduces backend CPU."},
  {"term": "Cloud CDN", "def": "Caches content at Google edge. Reduces latency for static content."}
]
-->
