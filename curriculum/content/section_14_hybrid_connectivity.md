# Week 2 Project: The Global Load Balancer

> **Objective**: Deploy a web application that survives a regional failure and routes users to the closest server.

## 🏗️ Architecture
```mermaid
graph TD
    User[🌍 User] -- Anycast IP --> GCLB[🌐 Global HTTP Load Balancer]
    GCLB -- US Traffic --> MIG_US[🇺🇸 Instance Group (US-Central1)]
    GCLB -- EU Traffic --> MIG_EU[🇪🇺 Instance Group (Europe-West1)]
```

## 📸 Expected Console Output
![Load Balancer Graph](https://placehold.co/800x450/e8f0fe/1d4ed8?text=GCP+Console:+Load+Balancing+Graph+showing+Traffic+distribution)
*Figure 1: Traffic flowing to both regions.*

## 🛠️ The Challenge
Your website "GlobalCat" is going viral. You need to ensure:
1.  Users in Europe get fast implementation.
2.  If the US region crashes, the site stays up.

## 🚀 Lab Steps
1.  **Instance Templates**: Create a template installing Nginx (`apt install -y nginx`).
2.  **Instance Groups (MIGs)**: 
    - Create `mig-us` in `us-central1`.
    - Create `mig-eu` in `europe-west1`.
3.  **Load Balancer**:
    - Select **HTTP(S) Load Balancing**.
    - Backend Service: Add both `mig-us` and `mig-eu`.
    - Frontend: Reserve a global IP.
4.  **Test**: Visit the IP.
5.  **Chaos Engineering**: "Stop" the US instances. Refresh. Access should seamlessly shift to EU (might take a moment for health checks).

## 🎯 Verification
Visit the IP address. You should see the "Welcome to nginx" page.
