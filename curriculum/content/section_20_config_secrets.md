# Day 20: ConfigMaps & Secrets

**Duration:** ⏱️ 45 Minutes  
**Level:** Intermediate  
**ACE Exam Weight:** ⭐⭐⭐ Medium

---

## 🎯 Learning Objectives

By the end of Day 20, learners will be able to:
*   **Decouple** configuration from code.
*   **Differentiate** between ConfigMaps and Secrets.
*   **Inject** an environment variable into a Pod.

---

## 🧠 1. The 12-Factor App Rule

**"Strictly separate config from code."**
You should NOT hardcode database passwords or API URLs in your Docker image.
Why? Because you want to use the *same* image for Dev, Test, and Prod.

### Kubernetes Objects:
1.  **ConfigMap:** For non-sensitive data (URLs, color themes, property files). Plain text.
2.  **Secret:** For sensitive data (Passwords, API Keys). Encoded (Base64) and obfuscated.

---

## 📔 2. Real-World Analogy: The Secret Diary

*   **ConfigMap** = **Sticky Note on the Fridge**.
    *   "Dinner is at 6 PM".
    *   Everyone can see it. It's useful info.
*   **Secret** = **My Diary**.
    *   "I have a crush on..."
    *   Locked. Only specific people (Pods) with the key can read it.

---

## 🛠️ 3. Hands-On Lab: Injecting Config

**🧪 Lab Objective:** Create a ConfigMap and read it from a Pod.

### ✅ Steps

1.  **Create ConfigMap:**
    ```bash
    kubectl create configmap game-config --from-literal=player_lives=3
    ```
2.  **Create a Pod (`pod-config.yaml`):**
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: mario
    spec:
      containers:
        - name: game
          image: alpine
          command: ["sleep", "3600"]
          env:
            - name: LIVES
              valueFrom:
                configMapKeyRef:
                  name: game-config
                  key: player_lives
    ```
    *(Run `nano pod-config.yaml`, paste above).*
3.  **Apply:** `kubectl apply -f pod-config.yaml`
4.  **Verify:**
    ```bash
    kubectl exec mario -- printenv LIVES
    ```
    *   *Result:* It prints "3". The container read the config!

---

## 📝 4. Quick Knowledge Check (Quiz)

1.  **Which object should you use to store a Database Password?**
    *   A. ConfigMap
    *   B. **Secret** ✅
    *   C. Pod Spec

2.  **Which object should you use to store a CSS theme color (public info)?**
    *   A. **ConfigMap** ✅
    *   B. Secret
    *   C. Volume

3.  **Why is it bad practice to hardcode config in a Docker Image?**
    *   A. It's slower.
    *   B. **You cannot easily change config between Dev/Prod without rebuilding the image.** ✅
    *   C. Docker doesn't support strings.

4.  **Secrets in Kubernetes are encrypted by default in ETCD (on GKE)?**
    *   A. No, they are just Base64 encoded.
    *   B. **Yes, GKE encrypts secrets at rest by default (Application Layer Secrets Encryption).** ✅
    *   C. Only if you pay extra.

5.  **How can a Pod consume a ConfigMap?**
    *   A. As Environment Variables.
    *   B. As a mounted Volume (file).
    *   C. **Both A and B.** ✅

---

<div class="checklist-card" x-data="{ 
    items: [
        { text: 'I describe why we separate config.', checked: false },
        { text: 'I created a ConfigMap.', checked: false },
        { text: 'I injected it as an Environment Variable.', checked: false }
    ]
}">
    <h3>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24" class="text-blurple">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        Day 20 Checklist
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
