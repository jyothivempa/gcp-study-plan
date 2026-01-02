# Day 15: Docker & Containers 101

**Duration:** ⏱️ 45 Minutes  
**Level:** Beginner  
**ACE Exam Weight:** ⭐⭐⭐ Foundation

---

## 🎯 Learning Objectives

By the end of Day 15, learners will be able to:
*   **Explain** what a Container is.
*   **Differentiate** between Virtual Machines (VMs) and Containers.
*   **Create** a `Dockerfile` and build an image.

---

## 🧠 1. What Is a Container?

A **Container** is a lightweight, standalone package of software that includes everything needed to run it: code, runtime, system tools, libraries, and settings.

### Containers vs VMs
*   **VM (Virtual Machine):** Has its own Guest OS. Heavy (GBs). Slow boot.
*   **Container:** Shares the Host OS kernel. Light (MBs). Instant start.

---

## 🍱 2. Real-World Analogy: The Lunchbox

*   **Your Code** = The Food (Sandwich & Apple).
*   **VM (Virtual Machine)** = **A Whole Kitchen**. 
    *   To transport your sandwich, you move the fridge, the oven, and the sink with it. Heavy!
*   **Container** = **A Lunchbox**.
    *   You only pack the food (App) and the spoon (Dependencies).
    *   It sits on any table (OS) and is ready to eat instantly.

---

## 🐳 3. Key Concepts

1.  **Dockerfile:** The recipe. A text file with instructions (`FROM python`, `COPY . .`).
2.  **Image:** The frozen meal. The result of building a Dockerfile. Read-only template.
3.  **Container:** The hot meal. A running instance of an Image.

---

## 🛠️ 4. Hands-On Lab: Build Your First Container

**🧪 Lab Objective:** Create a Docker container in Cloud Shell.

### ✅ Steps

1.  **Open Cloud Shell** (Top right in Console).
2.  **Create Directory:**
    ```bash
    mkdir my-docker-lab
    cd my-docker-lab
    ```
3.  **Create File:** `nano Dockerfile`
    ```dockerfile
    # Use lightweight Python
    FROM python:3.9-slim
    # Make a working directory
    WORKDIR /app
    # Create a dummy file
    RUN echo "Hello from Docker!" > message.txt
    # Command to run when starting
    CMD ["cat", "message.txt"]
    ```
4.  **Build Image:**
    ```bash
    docker build -t my-image:v1 .
    ```
5.  **Run Container:**
    ```bash
    docker run my-image:v1
    ```
    *   *Result:* It prints "Hello from Docker!" and exits.

---

## 📝 5. Quick Knowledge Check (Quiz)

1.  **Which statement best describes a Container?**
    *   A. A physical server.
    *   B. **A lightweight package including code and dependencies sharing the host OS.** ✅
    *   C. A full Virtual Machine with its own Kernel.

2.  **What is the "Recipe" file used to build a Docker Image?**
    *   A. `Makefile`
    *   B. `package.json`
    *   C. **`Dockerfile`** ✅

3.  **Main benefit of Containers vs VMs?**
    *   A. Containers are larger.
    *   B. **Containers start faster and use fewer resources.** ✅
    *   C. Containers are more secure by default.

4.  **How do you turn a Docker Image into a running application?**
    *   A. `docker build`
    *   B. `docker run` ✅
    *   C. `docker push`

5.  **Where does a Container run?**
    *   A. Only on Google Cloud.
    *   B. Only on Linux.
    *   C. **Anywhere with a Container Runtime (Laptop, Server, Cloud).** ✅

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I understand the Lunchbox analogy.', checked: false },
        { text: 'I created a Dockerfile.', checked: false },
        { text: 'I built an image with docker build.', checked: false },
        { text: 'I ran it with docker run.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 15 Checklist
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
