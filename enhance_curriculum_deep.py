
import os

CONTENT_DIR = r"d:\ultimateCode\gcp_study_plan\curriculum\content"

# Content map: Day -> Deep Dive Markdown
deep_dives = {
    1: """
## ⚡ Zero-to-Hero: Pro Tips
1.  **Organization Policies**:
    -   Unlike IAM (which says *who* can do *what*), Org Policies say *what resources* can be created.
    -   *Example:* "Restrict specific external IPs" or "Disable Service Account Key Creation".
    -   *Exam Tip:* If the question asks about "compliance restrictions," think Org Policy.
2.  **Resource Hierarchy Design**:
    -   Always use **Folders** to group environments (Dev, Test, Prod) or Departments.
    -   Map IAM at the Folder level to save time.
""",
    8: """
## ⚡ Zero-to-Hero: Advanced Networking
1.  **Shared VPC**:
    -   Host Project holds the Network. Service Projects connect to it.
    -   *Use Case:* One networking team manages the IP space; developers just attach instances.
2.  **Private Google Access (PGA)**:
    -   Allows VMs with **only private IPs** to reach Google APIs (like Storage, BigQuery) without going over the public internet.
    -   MUST be enabled on the **Subnet** level.
3.  **VPC Peering vs. VPN**:
    -   *Peering:* Connects two VPCs inside Google. Low latency. Non-transitive.
    -   *VPN:* Connects VPC to On-Premise (or other cloud). Slower, encrypted over internet.
""",
    12: """
## ⚡ Zero-to-Hero: Advanced IAM
1.  **Workload Identity Federation**:
    -   The modern way for AWS/Azure/On-Prem apps to talk to GCP *without* service account keys.
    -   *Mechanism:* Exchange an external OIDC token for a Google short-lived token.
2.  **IAM Conditions**:
    -   "Allow Alice to be an Editor, BUT ONLY from 9 AM to 5 PM."
    -   "Allow access ONLY if the request comes from this IP subnet."
3.  **Deny Policies**:
    -   GCP now supports IAM Deny policies (part of V2 IAM) which override any Allow rule. useful for centralized guardrails.
""",
    15: """
## ⚡ Zero-to-Hero: Cloud Shell Power
1.  **Boost Mode**:
    -   Cloud Shell is a small VM (e2-small). You can temporarily "Boost" it to be faster for 24 hours.
2.  **Web Preview**:
    -   Run a web server on port 8080 in Cloud Shell, and you can preview it securely via browser proxy.
3.  **Persistent Storage**:
    -   The `$HOME` directory (5GB) persists. Everything else (system packages) is lost on restart.
""",
    18: """
## ⚡ Zero-to-Hero: GKE Architecture
1.  **Standard vs. Autopilot**:
    -   *Standard:* You manage Nodes (VMs). You pay for Nodes (even if empty).
    -   *Autopilot:* Google manages Nodes. You pay ONLY for Pod resources (CPU/RAM requested).
2.  **Private Clusters**:
    -   Nodes have NO public IPs. Control Plane access is restricted.
    -   *Security requirement* for most enterprises.
""",
    23: """
## ⚡ Zero-to-Hero: Database Scaling
1.  **Spanner vs. Cloud SQL**:
    -   *Choose Spanner* if: You need > 30TB data, Global Consistency, or Unlimited scaling.
    -   *Choose Cloud SQL* if: You fit in a single region (mostly), need legacy compatibility (MySQL/Postgres tools).
2.  **Bigtable Key Design**:
    -   The "Row Key" is the ONLY way to retrieve data efficiently.
    -   *Anti-Pattern:* Sequential keys (timestamps) cause "Hotspotting". Use Hashing.
"""
}

def enhance_files():
    files = sorted(os.listdir(CONTENT_DIR))
    for filename in files:
        if not filename.endswith(".md"):
            continue
            
        # Extract day number roughly
        parts = filename.split("_")
        try:
            day_num = int(parts[1])
        except (ValueError, IndexError):
            continue

        filepath = os.path.join(CONTENT_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if already enhanced
        if "## ⚡ Zero-to-Hero" in content:
            print(f"Skipping {filename} (Already Enhanced)")
            continue

        # Get generic or specific enhancement
        enhancement = deep_dives.get(day_num, "")
        
        # Generic fallback if no specific deep dive but we want to add a footer stamp
        if not enhancement:
             enhancement = f"""
## ⚡ Zero-to-Hero: Pro Tips
*   **CLI Command**: Practice `gcloud {parts[2] if len(parts)>2 else 'services'} list` to see resources via command line.
*   **Real World**: In production, prefer **Terraform** over clicking in the console for {parts[2] if len(parts)>2 else 'this resource'}.
"""

        # Append before Flashcards or at end
        if "<!-- FLASHCARDS" in content:
            new_content = content.replace("<!-- FLASHCARDS", f"{enhancement}\n\n<!-- FLASHCARDS")
        else:
            new_content = content + "\n" + enhancement

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Enhanced {filename}")

if __name__ == "__main__":
    enhance_files()
