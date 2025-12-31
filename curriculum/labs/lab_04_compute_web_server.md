
# 🛠️ Lab 04: Host a Website on Compute Engine

**Objective:** Deploy a simple web server using a Startup Script and verify access.
**Duration:** 15 Minutes

## 1. Create the Virtual Machine
Run this command in **Cloud Shell** (or use the Console):

```bash
gcloud compute instances create my-web-server \
    --zone=us-central1-a \
    --machine-type=e2-micro \
    --tags=http-server \
    --metadata=startup-script='#! /bin/bash
apt-get update
apt-get install -y nginx
echo "<h1>Hello from Google Cloud!</h1>" > /var/www/html/index.html'
```

*   **Zone:** We pinned it to `us-central1-a`.
*   **Tags:** `http-server` (We will use this for the firewall).
*   **Startup Script:** Automatically installs Nginx and creates a custom `index.html`.

## 2. Create Firewall Rule
By default, external web traffic is blocked. Open port 80:

```bash
gcloud compute firewall-rules create allow-http-traffic \
    --direction=INGRESS \
    --priority=1000 \
    --network=default \
    --action=ALLOW \
    --rules=tcp:80 \
    --source-ranges=0.0.0.0/0 \
    --target-tags=http-server
```

## 3. Verify Success
Find your VM's External IP:
```bash
gcloud compute instances list
```

Copy the **EXTERNAL_IP** and paste it into your browser tab: `http://<YOUR_IP>`

**Expected Result:** You should see a big bold **"Hello from Google Cloud!"**.

## 🧹 Cleanup
```bash
gcloud compute instances delete my-web-server --zone=us-central1-a --quiet
gcloud compute firewall-rules delete allow-http-traffic --quiet
```
