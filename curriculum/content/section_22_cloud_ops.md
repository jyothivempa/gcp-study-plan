# Day 22: Cloud Operations (Monitoring & Logging)

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐⭐ High

---

## 🎯 Learning Objectives

By the end of Day 22, learners will be able to:
*   **Differentiate** between Cloud Monitoring (Metrics) and Cloud Logging (Text).
*   **Create** an Uptime Check for a website.
*   **Install** the Ops Agent on a VM.

---

## 🧠 1. The "Day 2" Problem

You built an app. It works.
3 weeks later, users say it's "slow".
How do you know *why*?

**Google Cloud Operations Suite** (formerly Stackdriver) gives you visibility.

### Key Components:
1.  **Cloud Monitoring:** Graphs & Charts. (CPU usage, Disk I/O).
2.  **Cloud Logging:** Text records. ("Error: Database failed").
3.  **Error Reporting:** Aggregates crashes. ("NullPointerException happened 500 times").

---

## 🚗 2. Real-World Analogy: The Car Dashboard

*   **Cloud Monitoring** = **The Speedometer & Gauges**.
    *   It tells you numbers: "Speed is 60mph". "Fuel is 10%".
    *   It does NOT tell you *why* fuel is low.
*   **Cloud Logging** = **The Black Box / Flight Recorder**.
    *   It records events: "12:00 PM - Driver filled tank".
*   **Alerting** = **Check Engine Light**.
    *   It screams at you when something crosses a threshold (Temp > 200°C).

---

## 🛠️ 3. Hands-On Lab: Install Ops Agent

**🧪 Lab Objective:** Get Memory metrics from a VM (Memory is NOT visible by default!).

### ✅ Steps

1.  **Create VM:** `gcloud compute instances create monitor-demo --zone=us-central1-a`
2.  **Go to Console:** **Monitoring** > **Dashboards**.
    *   *Notice:* You can see CPU, but you get "No Data" for Memory utilization. Why?
    *   *Reason:* The Hypervisor sees CPU, but it cannot see *inside* the OS RAM.
3.  **Install Agent:**
    *   SSH into the VM.
    *   Run:
        ```bash
        curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
        sudo bash add-google-cloud-ops-agent-repo.sh --also-install
        ```
4.  **Verify:** Wait 5 mins. Check Monitoring again. You now see Memory!
5.  **Create Uptime Check:**
    *   Go to **Monitoring** > **Uptime Checks**.
    *   Target: `monitor-demo` (External IP).
    *   Frequency: 1 min.
    *   Wait... It will turn green. Google is pinging your VM globally.

---

## 📝 4. Quick Knowledge Check (Quiz)

1.  **Which service is used to visualize numeric data like CPU %?**
    *   A. Cloud Logging
    *   B. **Cloud Monitoring** ✅
    *   C. Cloud Trace

2.  **You need to get an email if your VM CPU stays above 90% for 5 minutes. What do you create?**
    *   A. An Uptime Check
    *   B. **An Alerting Policy** ✅
    *   C. A Dashboard

3.  **Why can't you see Memory/RAM usage for a standard VM by default?**
    *   A. It costs extra.
    *   B. **The Hypervisor cannot read the Guest OS memory. You need the Ops Agent.** ✅
    *   C. Google hides it.

4.  **How do you check if your web server is reachable from Asia and Europe?**
    *   A. **Create a global Uptime Check.** ✅
    *   B. SSH into it.
    *   C. Ask a friend in Asia.

5.  **Cloud Logging is best used for:**
    *   A. Detecting trends.
    *   B. **Searching for specific error messages (Text).** ✅
    *   C. Billing.

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I describe the difference between Metrics (Monitoring) and Text (Logging).', checked: false },
        { text: 'I know why we need the Ops Agent (Memory/Disk Space).', checked: false },
        { text: 'I installed the Agent.', checked: false },
        { text: 'I created an Uptime Check.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 22 Checklist
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
