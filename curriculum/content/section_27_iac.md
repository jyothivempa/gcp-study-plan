# Day 27: Infrastructure as Code (Terraform)

**Duration:** ⏱️ 45 Minutes  
**Level:** Advanced  
**ACE Exam Weight:** ⭐⭐ Low (But growing)

---

## 🎯 Learning Objectives

By the end of Day 27, learners will be able to:
*   **Define** IaC (Infrastructure as Code).
*   **Compare** Imperative (gcloud) vs Declarative (Terraform).
*   **Read** a basic Terraform file.

---

## 🧠 1. Why Code?

Clicking in the Console is fun for Day 1.
It is a nightmare for Day 100.
*   "Did Bob enable the firewall? Or was it Alice?"
*   "We need to create the exact same environment in Europe. Do we click 500 times again?"

**Solution:** **Infrastructure as Code (IaC)**.
You write a text file describing your infra. You run a tool. The tool builds it.

---

## 🏡 2. Real-World Analogy: The Blueprint

*   **Console/gcloud** = **Building a house by shouting.**
    *   "Put a brick there! Wait, move it left!"
    *   Hard to replicate.
*   **Terraform** = **The Blueprint**.
    *   You give the contractor a drawing.
    *   It shows *exactly* what the final house should look like.
    *   You can give the same blueprint to another contractor to build a clone.

---

## ⚔️ 3. Imperative vs Declarative

*   **Imperative (gcloud / Script):** "Step 1: Create VM. Step 2: Add Disk."
    *   *Problem:* If you run it twice, you get 2 VMs (or an error).
*   **Declarative (Terraform):** "I want 1 VM to exist."
    *   *Benefit:* If you run it twice, Terraform says "It already exists. Nothing to do." (Idempotent).

---

## 🛠️ 4. Hands-On Lab: Read Terraform

*Note: We won't install Terraform today (it takes too long), but we will analyze the code.*

**main.tf:**
```hcl
resource "google_compute_instance" "default" {
  name         = "my-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
  }
}
```

*   **resource:** What we are creating.
*   **google_compute_instance:** The GCP resource type.
*   **"default":** The local name in code.
*   **properties:** The inputs (name, zone).

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **What is the main benefit of Infrastructure as Code?**
    *   A. It's faster to write once.
    *   B. **Reproducibility and Version Control (Git).** ✅
    *   C. It requires knowing Python.

2.  **Which Google Cloud native tool is similar to Terraform?**
    *   A. Cloud Build
    *   B. **Deployment Manager** ✅
    *   C. Cloud Spanner

3.  **Terraform is:**
    *   A. Imperative (Step-by-step).
    *   B. **Declarative (End-state description).** ✅

4.  **If you run a Terraform apply command twice, what happens?**
    *   A. It duplicates resources.
    *   B. **It does nothing the second time (Idempotent), because the state matches.** ✅
    *   C. It deletes resources.

5.  **Where do you store your Terraform files?**
    *   A. In a bucket.
    *   B. **In a Version Control System (like GitHub).** ✅
    *   C. On a USB drive.

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I understand why clicking in the console is bad for Prod.', checked: false },
        { text: 'I know the difference between Imperative and Declarative.', checked: false },
        { text: 'I can identify a Resource in a Terraform file.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 27 Checklist
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
