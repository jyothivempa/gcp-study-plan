# WEEK 2 REVIEW: Networking

## 🧠 Mental Map Recap (The "City" Analogy)
1.  **VPC:** The **Planet**. Global. Contains all your networking.
2.  **Subnet:** The **City**. Regional. Defined by IP ranges (CIDR).
3.  **Firewall:** The **Security Guard**. Rules allowing Ingress/Egress.
4.  **Load Balancer:** The **Traffic Cop**. Distributes users to servers.
    *   *HTTP LB:* Smart (Layer 7), Global.
    *   *TCP LB:* Fast (Layer 4), Regional.
5.  **Cloud NAT:** The **One-Way Mirror**. Allows private VMs to talk out, but blocks internet from talking in.

## 🚨 Top 3 Beginner Mistakes
1.  **The "Global Subnet" Myth:** "I want a subnet that spans US and Europe." *Impossible. Subnets are Regional.*
2.  **The Firewalled VM:** "I created a firewall rule but it doesn't work." *Did you add the Network Tag to the VM?*
3.  **The SSH Trap:** "I can't SSH into my private VM." *Cloud NAT is outbound only. You need IAP or a Bastion Host.*

## 📝 Network Mock Exam (10 Questions)

**Q1. You want to deploy a web application to users globally. You need a single IP address that routes users to the closest datacenter. Which Load Balancer should you choose?**
*   A. Network TCP Load Balancer.
*   B. Internal HTTP Load Balancer.
*   C. External Global HTTP(S) Load Balancer.
*   D. UDP Load Balancer.
> **Correct Answer: C.** *Global HTTP LB provides Anycast IP and global routing.*

**Q2. You have a VM in a private subnet. It needs to download security patches from the internet. It must NOT have a public IP address. What do you configure?**
*   A. Cloud VPN.
*   B. Cloud NAT.
*   C. VPC Peering.
*   D. External Load Balancer.
> **Correct Answer: B.** *Cloud NAT provides outbound internet access for private VMs.*

**Q3. A firewall rule with Priority 1000 allows traffic on Port 80. A rule with Priority 100 denies traffic on Port 80. What happens?**
*   A. Traffic is Allowed.
*   B. Traffic is Denied.
*   C. Traffic is allowed only for Admins.
*   D. The rules conflict and error out.
> **Correct Answer: B.** *Lower priority number wins. 100 overrides 1000.*

**Q4. Can a VPC span multiple regions?**
*   A. No, VPCs are Zonal.
*   B. No, VPCs are Regional.
*   C. Yes, VPCs are Global.
*   D. Only if you use VPC Peering.
> **Correct Answer: C.** *GCP VPCs are global resources.*

**Q5. You need to restrict access to a database server so only the "Web Server" group can connect. What is the best practice?**
*   A. Create a firewall rule allowing the specific IP addresses of the web servers.
*   B. Create a firewall rule allowing traffic from `0.0.0.0/0`.
*   C. Add a Network Tag "web-server" to the web VMs, and allow ingress from that Tag.
*   D. Put them in the same Zone.
> **Correct Answer: C.** *Using Tags is more scalable than managing static IP lists.*

**Q6. What is the default route (0.0.0.0/0) used for?**
*   A. Routing traffic to the local subnet.
*   B. Routing traffic to the Internet Gateway.
*   C. Routing traffic to Google Services (APIs).
*   D. Routing traffic to a VPN.
> **Correct Answer: B.** *It directs traffic to the internet.*

**Q7. Which Load Balancer is best for non-HTTP traffic (e.g., a Database or Gaming Server)?**
*   A. HTTP(S) Load Balancer.
*   B. Network (TCP/UDP) Load Balancer.
*   C. SSL Proxy Load Balancer.
*   D. Cloud CDN.
> **Correct Answer: B.** *TCP/UDP LB handles raw traffic.*

**Q8. True or False: You can expand the IP range of a subnet after it has been created.**
*   A. True.
*   B. False.
> **Correct Answer: A.** *You can expand (increase) the CIDR range without downtime.*

**Q9. If you delete a VPC, what happens to the Subnets inside it?**
*   A. They are moved to the "Default" VPC.
*   B. They are deleted.
*   C. They become orphaned resources.
*   D. Nothing, Subnets are independent.
> **Correct Answer: B.** *Subnets are child resources of the VPC.*

**Q10. You are creating a custom VPC. How many subnets does it have by default?**
*   A. One per region.
*   B. One per zone.
*   C. Zero.
*   D. Ten.
> **Correct Answer: C.** *Custom VPCs start empty.*

## ✅ Confidence Checklist
*   [ ] I can explain why we use NAT (Security).
*   [ ] I know the difference between Global (HTTP) and Regional (TCP) Loading Balancing.
*   [ ] I know that "Allow 0.0.0.0/0" is bad practice.
*   [ ] I understand that Tags make firewall rules easier.
*   [ ] I scored 8/10 on the mock exam.

**READY?**
If you passed, get ready for **Week 3: Security & IAM**. We will learn who (Identities) can do what (Roles).


<!-- FLASHCARDS
[
  {
    "term": "Week 2 Focus",
    "def": "Networking and Security (IAM)."
  },
  {
    "term": "Hops",
    "def": "Steps traffic takes. Internet -> LB -> VM."
  },
  {
    "term": "Public vs Private",
    "def": "Public = Internet reachable. Private = VPC only."
  },
  {
    "term": "Role Binding",
    "def": "Connecting User + Role + Resource."
  },
  {
    "term": "Service Account",
    "def": "Identity for Apps."
  }
]
-->
