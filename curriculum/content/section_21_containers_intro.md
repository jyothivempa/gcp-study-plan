# SECTION 21: Containers 101 (Before GKE)

> **Official Doc Reference**: [Containers Concepts](https://cloud.google.com/containers)

## 1️⃣ What is a Container? 📦
Think of a traditional **Virtual Machine (VM)** as a "House".
*   It has its own plumbing, electricity, and foundation (Guest OS).
*   It's heavy. Takes time to build.

Think of a **Container** as an "Apartment" in a Hotel.
*   The Hotel (Host OS) provides the plumbing and foundation.
*   You just bring your furniture (Code & Dependencies).
*   It's lightweight. Moves in seconds.

## 2️⃣ Why not just use VMs?
*   **Speed:** VM boots in MINUTES. Container boots in MILLISECONDS.
*   **Portability:** "It works on my machine" -> It works in Production.
*   **Density:** You can run 100 containers on a server that could only hold 5 VMs.

## 3️⃣ Docker Basics (The Engine) 🐳
Docker is the tool that builds and runs containers.
*   **Dockerfile:** The recipe (instruction manual).
*   **Image:** The cake (the built artifact).
*   **Container:** The slice of cake being eaten (the running instance).

### Key Commands (Exam)
*   `docker build -t my-app .` -> Build image.
*   `docker run -p 80:80 my-app` -> Run image.
*   `docker push gcr.io/project/my-app` -> Push to Google Container Registry.

## 4️⃣ Hands-On Lab: Build Your First Container 🛠️
1.  **Open Cloud Shell**.
2.  **Create a file named `Dockerfile`**:
    ```dockerfile
    FROM python:3.9-slim
    WORKDIR /app
    COPY . .
    CMD ["python", "-c", "print('Hello from a Container!')"]
    ```
3.  **Build It**:
    ```bash
    docker build -t hello-container .
    ```
4.  **Run It**:
    ```bash
    docker run hello-container
    ```
    *Output:* `Hello from a Container!`

## 5️⃣ Checkpoint Quiz
<form>
  <div class="quiz-question" id="q1">
    <p class="font-bold">1. Which file is used to define how to build a Docker image?</p>
    <div class="space-y-2">
      <label class="block"><input type="radio" name="q1" value="wrong"> build.yaml</label>
      <label class="block"><input type="radio" name="q1" value="correct"> Dockerfile</label>
      <label class="block"><input type="radio" name="q1" value="wrong"> container.json</label>
    </div>
  </div>
</form>
