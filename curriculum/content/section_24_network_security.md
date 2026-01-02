# Day 24: Network Security (Firewalls & IAP)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐ High

---

## 🎯 Learning Objectives

By the end of Day 24, learners will be able to:
*   **Configure** Firewall Rules (Ingress/Egress).
*   **Use** Identity-Aware Proxy (IAP) for secure SSH (No VPN needed!).
*   **Explain** Cloud Armor (DDoS protection).

---

## 🧠 1. Firewall Rules

By default, **Incoming (Ingress)** is Blocked. **Outgoing (Egress)** is Allowed.
You need rules to open ports.

### Anatomy of a Rule:
*   **Direction:** Ingress or Egress.
*   **Priority:** 1000 (Lower number = Higher priority).
*   **Target:** "All instances" OR "Tags" (e.g., `web-server`).
*   **Source Filter:** IP Ranges (`0.0.0.0/0` = Internet).

---

## 🏰 2. Real-World Analogy: The Drawbridge

*   **VPC** = **The Castle**.
*   **Firewall** = **The Drawbridge Guard**.
    *   He checks every person (Packet).
    *   "Are you on the list?" (Rule: Allow Port 80).
    *   "No? Go away." (Deny).
*   **IAP (Identity-Aware Proxy)** = **The Secret Tunnel**.
    *   Instead of opening the main gate (Public IP) for admins to SSH in...
    *   Google checks your ID badge at a separate secure door, then teleports you inside. No public IP needed on the VM!

---

## 🛡️ 3. Identity-Aware Proxy (IAP)

**The Problem:** You want to SSH into a VM, but you don't want to expose Port 22 to the evil internet.
**The Fix:** IAP.
1.  You allow ingress from Google's IP range (`35.235.240.0/20`).
2.  You click "SSH" in the console.
3.  Google authenticates you (Gmail).
4.  Google tunnels traffic to your VM's internal IP.
**Result:** Secure SSH with NO Public IP on the VM.

---

## 🛠️ 4. Hands-On Lab: Secure SSH with IAP

**🧪 Lab Objective:** SSH into a VM that has NO Public IP.

### ✅ Steps

1.  **Create VM (Private):**
    *   Name: `private-vm`.
    *   **Network Interface:** Click pencil icon.
    *   **External IPv4 address:** Select **None**. (This is scary!).
    *   Create.
2.  **Try to Connect:**
    *   Click SSH. -> **Connection Failed**. (It can't reach it).
3.  **Create Firewall Rule:**
    *   VPC Network > Firewall > Create Firewall Rule.
    *   Name: `allow-iap`.
    *   Targets: All instances.
    *   Source IPv4 ranges: `35.235.240.0/20` (This is Google's Magic IAP Range).
    *   Protocols: TCP: 22.
    *   Create.
4.  **Try SSH Again:**
    *   Click SSH. -> **Success!**
    *   You are now inside a completely private VM via the "Secret Tunnel".

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **If you create a VM with NO External IP, how can you SSH into it without a VPN?**
    *   A. You cannot.
    *   B. **Identity-Aware Proxy (IAP)** ✅
    *   C. Port Forwarding.

2.  **What is the default Firewall behavior for Ingress (Incoming) traffic?**
    *   A. Allow All
    *   B. **Deny All (Implicit Deny)** ✅
    *   C. Allow HTTP

3.  **For a Firewall Rule to apply to only specific VMs, what should you use?**
    *   A. Network Tags (Target Tags).
    *   B. VM Name.
    *   C. Disk Size.

4.  **Which Google service protects your Load Balancer from DDoS attacks and SQL Injection?**
    *   A. Cloud NAT
    *   B. **Cloud Armor** ✅
    *   C. VPC Peering

5.  **In a Firewall Rule, does a LOWER Priority number mean it is evaluated first or last?**
    *   A. Last (1000 overrides 1)
    *   B. **First (1 overrides 1000)** ✅

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I understand how Priorities work.', checked: false },
        { text: 'I created a VM with no Public IP.', checked: false },
        { text: 'I set up the IAP firewall rule (35.235.240.0/20).', checked: false },
        { text: 'I used IAP to SSH.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 24 Checklist
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
