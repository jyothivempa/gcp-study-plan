
# 🛠️ Lab 11: Global HTTP Load Balancer

**Objective:** Deploy a Global Load Balancer fronting a Managed Instance Group (MIG).
**Duration:** 25 Minutes

## 1. Create Instance Template
Defines what our VMs look like (Apache Web Server).

```bash
gcloud compute instance-templates create my-web-template \
  --region=us-central1 \
  --tags=lb-backend \
  --metadata=startup-script='#! /bin/bash
    apt-get update
    apt-get install -y apache2
    echo "Served from: $HOSTNAME" > /var/www/html/index.html'
```

## 2. Create Managed Instance Group (MIG)
Creates 2 replicas automatically.

```bash
gcloud compute instance-groups managed create my-mig \
    --template=my-web-template \
    --size=2 \
    --zone=us-central1-a
```

## 3. Set Named Port
Tell the MIG that "http" service is on port 80.
```bash
gcloud compute instance-groups set-named-ports my-mig \
    --named-ports http:80 \
    --zone=us-central1-a
```

## 4. Create Firewall
 Allow Health Checks from Google (ranges 130.211.0.0/22 and 35.191.0.0/16).

```bash
gcloud compute firewall-rules create allow-health-check \
    --allow tcp:80 \
    --source-ranges 130.211.0.0/22,35.191.0.0/16 \
    --target-tags lb-backend
```

## 5. Configure the Load Balancer (Complex!)
This involves 4 pieces: Health Check, Backend Service, URL Map, Proxy, Forwarding Rule.

```bash
# 1. Health Check
gcloud compute health-checks create http http-basic-check --port 80

# 2. Backend Service
gcloud compute backend-services create my-web-backend \
    --protocol HTTP \
    --health-checks http-basic-check \
    --global

# 3. Add MIG to Backend
gcloud compute backend-services add-backend my-web-backend \
    --instance-group=my-mig \
    --instance-group-zone=us-central1-a \
    --global

# 4. URL Map (The Router)
gcloud compute url-maps create my-web-map --default-service my-web-backend

# 5. HTTP Proxy
gcloud compute target-http-proxies create my-http-proxy --url-map my-web-map

# 6. Global Forwarding Rule (The Front Door / IP)
gcloud compute forwarding-rules create my-http-rule \
    --target-http-proxy=my-http-proxy \
    --ports=80 \
    --global
```

## 6. Verify
Get the IP:
```bash
gcloud compute forwarding-rules list
```
Wait ~5 minutes for propagation. Visit the IP. Refresh multiple times.
**Expected:** You should see "Served from: my-mig-xxxx" changing as it balances traffic!

## 🧹 Cleanup
*(Delete strictly in reverse order to avoid dependency errors)*
```bash
gcloud compute forwarding-rules delete my-http-rule --global --quiet
gcloud compute target-http-proxies delete my-http-proxy --quiet
gcloud compute url-maps delete my-web-map --quiet
gcloud compute backend-services delete my-web-backend --global --quiet
gcloud compute health-checks delete http-basic-check --quiet
gcloud compute instance-groups managed delete my-mig --zone=us-central1-a --quiet
gcloud compute instance-templates delete my-web-template --quiet
```
