
# 🛠️ Lab 18: Deploy App to GKE (Kubernetes)

**Objective:** Create a GKE Autopilot cluster and deploy a containerized Nginx application.
**Duration:** 30 Minutes

## 1. Create GKE Cluster (Autopilot)
Autopilot manages the nodes for you. It's the easiest way to start.

```bash
gcloud container clusters create-auto my-cluster \
    --region us-central1
```
*(This may take 5-10 minutes. Go grab a coffee ☕)*

## 2. Get Credentials
Configure `kubectl` to talk to this cluster.
```bash
gcloud container clusters get-credentials my-cluster --region us-central1
```

## 3. Deploy an Application
We will create a **Deployment** (runs the pods) running a simple `hello-app`.

```bash
kubectl create deployment hello-server \
    --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
```

## 4. Expose it (Load Balancer)
We need an External IP to see it. Create a **Service** of type LoadBalancer.

```bash
kubectl expose deployment hello-server \
    --type=LoadBalancer \
    --port 8080
```

## 5. Verify
Watch for the External IP to be assigned:
```bash
kubectl get service hello-server --watch
```
When `EXTERNAL-IP` changes from `<pending>` to a real IP, copy it.
Visit: `http://<EXTERNAL_IP>:8080`

**Expected Result:** "Hello, world! Version: 1.0.0. Hostname: hello-server-xxxx"

## 6. Scale It Up!
Simulate traffic demand by creating more replicas.
```bash
kubectl scale deployment hello-server --replicas=5
kubectl get pods
```
You will see 5 pods running.

## 🧹 Cleanup
```bash
kubectl delete service hello-server
gcloud container clusters delete my-cluster --region us-central1 --quiet
```
