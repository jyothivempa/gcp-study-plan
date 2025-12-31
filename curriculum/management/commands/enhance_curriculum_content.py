import os

BASE_PATH = r'C:\Users\JYOTHI\.gemini\antigravity\brain\4410c013-0004-4b8c-9631-9ccdf699cfbf'

# DATA: Specific enhancements for each section file
# We are adding "Interview-Ready Q&A" and "Key Terminology" if missing.
ENHANCEMENTS = {
    'section_4_compute_engine.md': """
## 8️⃣ Interview-Ready Q&A
**Q: "When would you choose a Preemptible VM over a standard one?"**
*   **A:** For fault-tolerant batch processing jobs or testing where cost saving (up to 80%) is more important than uptime. Never for a database or production API.

**Q: "How do you resize a VM without deleting it?"**
*   **A:** You must Stop the instance, edit the Machine Type, and Start it again. You cannot resizing CPU/RAM while it is running.
""",
    'section_5_storage_basics.md': """
## 8️⃣ Interview-Ready Q&A
**Q: "What is the difference between Local SSD and Persistent Disk?"**
*   **A:** Local SSD is physically attached to the server (super fast, but data is lost if VM stops). Persistent Disk is network storage (slower, but durable and survives VM stops).

**Q: "Can I attach one Persistent Disk to multiple VMs?"**
*   **A:** Yes, in "Read Only" mode. For Read-Write, it typically attaches to only one VM (unless using multi-writer mode which is complex/niche).
""",
    'section_6_cloud_storage.md': """
## 8️⃣ Interview-Ready Q&A
**Q: "I uploaded a file to a bucket but my colleague can't see it. Why?"**
*   **A:** Permissions are set at the Bucket level or Object level. Check IAM roles. Also, objects are private by default.

**Q: "When should I use 'Coldline' vs 'Archive'?"**
*   **A:** Coldline is for data accessed once a quarter (e.g., 90 days). Archive is for data accessed less than once a year (e.g., Regulatory backups). Archive is cheaper for storage but more expensive for retrieval.
""",
    'section_8_vpc_basics.md': """
## 8️⃣ Interview-Ready Q&A
**Q: "Is a VPC global or regional?"**
*   **A:** The VPC *object* is Global. You can have subnets in US and Asia inside the same VPC. However, *Subnets* are Regional.

**Q: "What happens if I create a VM without specifying a network?"**
*   **A:** It defaults to the 'default' VPC. If you deleted the default VPC, the creation fails.
""",
    'section_9_subnets_ip.md': """
## 8️⃣ Interview-Ready Q&A
**Q: "Can I expand a subnet range after creation?"**
*   **A:** Yes, you can expand (increase) the CIDR range without downtime. You *cannot* shrink it.

**Q: "What is the smallest subnet I can create in GCP?"**
*   **A:** /29 (giving you very few usable IPs). The largest is /8 (huge).
""",
    'section_10_firewall_rules.md': """
## 8️⃣ Interview-Ready Q&A
**Q: "I applied a firewall rule to a tag, but it's not working. Why?"**
*   **A:** Did you restart the application? (Just kidding). Check if the VM actually has the tag. Tags are case-sensitive! Also check for higher priority deny rules.

**Q: "How do I allow traffic from a specific load balancer?"**
*   **A:** Use the Google Cloud Load Balancer's source IP ranges (130.211.0.0/22 and 35.191.0.0/16) in your ingress rule.
""",
     'section_11_load_balancing.md': """
## 8️⃣ Interview-Ready Q&A
**Q: "Difference between L4 and L7 Load Balancing?"**
*   **A:** L4 (TCP/UDP) makes decisions based on IP/Port (faster, dumber). L7 (HTTP/HTTPS) makes decisions based on content (URL path, headers, cookies) - smarter but more processing.

**Q: "What is a Global Load Balancer?"**
*   **A:** It gives you a single Anycast IP. Users all over the world hit this one IP, and Google routes them to the closest backend.
""",
      'section_12_iam_core.md': """
## 8️⃣ Interview-Ready Q&A
**Q: "Difference between Primitive and Predefined Roles?"**
*   **A:** Primitive (Owner/Editor/Viewer) are too broad and dangerous. Predefined (Storage Admin, Compute Viewer) are granular and recommended.

**Q: "What is 'Policy Hierarchy'?"**
*   **A:** Policies inherit downwards. Org -> Folder -> Project -> Resource. A 'Deny' at the top overrides 'Allow' at the bottom (mostly). Actually, 'Allow' is additive, but 'Deny' policies (if using organization policies) restrict what can be done.
""",
}

def update_file(filename, content_to_add):
    full_path = os.path.join(BASE_PATH, filename)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if "Interview-Ready Q&A" already exists to avoid duplication
        if "## 8️⃣ Interview-Ready Q&A" in content:
            print(f"Skipping {filename}: Already has Interview Q&A.")
            return

        # Insert before "## 8️⃣ Checkpoint Questions" or "## 9️⃣ One-Line Memory Hook"
        insertion_point = "## 8️⃣ Checkpoint Questions"
        if insertion_point not in content:
            insertion_point = "## 🚨 Checkpoint Questions" # Handle variation
        
        if insertion_point in content:
            new_content = content.replace(insertion_point, content_to_add + "\n\n" + insertion_point)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename} with Interview Q&A.")
        else:
            print(f"Warning: Could not find insertion point in {filename}")

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")

def handle():
    print("Starting Bulk Content Upgrade...")
    for filename, extra_content in ENHANCEMENTS.items():
        update_file(filename, extra_content)
    print("Bulk Upgrade Complete.")

if __name__ == "__main__":
    handle()
