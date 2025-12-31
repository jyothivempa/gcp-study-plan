
# 🛠️ Lab 08: VPC Peering & Connectivity

**Objective:** Connect two isolated VPC Networks using VPC Peering and verify ping connectivity.
**Duration:** 20 Minutes

## 1. Create Two VPCs
We need two separate networks to simulate two companies or departments.

```bash
# Create Network A
gcloud compute networks create vpc-a --subnet-mode=custom
gcloud compute networks subnets create subnet-a --network=vpc-a --region=us-central1 --range=10.0.1.0/24

# Create Network B
gcloud compute networks create vpc-b --subnet-mode=custom
gcloud compute networks subnets create subnet-b --network=vpc-b --region=us-central1 --range=10.0.2.0/24
```

## 2. Create Firewalls to Allow SSH & Ping
```bash
# Allow SSH/ICMP on VPC A
gcloud compute firewall-rules create vpc-a-allow-internal \
    --network=vpc-a --allow=tcp:22,icmp --source-ranges=0.0.0.0/0

# Allow SSH/ICMP on VPC B
gcloud compute firewall-rules create vpc-b-allow-internal \
    --network=vpc-b --allow=tcp:22,icmp --source-ranges=0.0.0.0/0
```

## 3. Create VMs in Each VPC
```bash
gcloud compute instances create vm-a --network=vpc-a --subnet=subnet-a --zone=us-central1-a
gcloud compute instances create vm-b --network=vpc-b --subnet=subnet-b --zone=us-central1-a
```

## 4. Test Connectivity (Fail)
1.  SSH into `vm-a`.
2.  Try to ping the internal IP of `vm-b` (likely `10.0.2.2`).
3.  **Result:** It will FAIL (Hang). The networks are isolated.

## 5. Enable VPC Peering
Peer them together. Peering is non-transitive and requires setup on **BOTH** sides.

```bash
# Connect A to B
gcloud compute networks peerings create peer-ab --network=vpc-a --peer-network=vpc-b

# Connect B to A
gcloud compute networks peerings create peer-ba --network=vpc-b --peer-network=vpc-a
```

## 6. Test Connectivity (Success)
1.  SSH into `vm-a` again.
2.  Ping `vm-b` IP (`10.0.2.2`).
3.  **Result:** It works! 🚀

## 🧹 Cleanup
```bash
gcloud compute instances delete vm-a vm-b --zone=us-central1-a --quiet
gcloud compute networks subnets delete subnet-a --region=us-central1 --quiet
gcloud compute networks subnets delete subnet-b --region=us-central1 --quiet
gcloud compute networks delete vpc-a --quiet
gcloud compute networks delete vpc-b --quiet
```
