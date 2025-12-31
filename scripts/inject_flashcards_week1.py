import os
import json

# Define Flashcards for Week 1 (Days 1-7)
FLASHCARDS_DATA = {
    "section_1_cloud_foundations.md": [
        {"term": "Project ID", "def": "The globally unique, immutable identifier for your project. Used in CLI/Terraform."},
        {"term": "Organization Node", "def": "The root node for a company. Not available for @gmail.com users."},
        {"term": "Folder", "def": "A grouping of projects (e.g., by Department). Policies inherit down from here."},
        {"term": "Zonal Resource", "def": "Lives in 1 Zone. Dies if zone fails. Ex: VM, Persistent Disk."},
        {"term": "Global Resource", "def": "Available everywhere. Ex: VPC Network, Firewall Rules, IAM."}
    ],
    "section_2_gcp_structure.md": [
        {"term": "Region", "def": "A geographical location (e.g., Iowa) containing 3+ Zones."},
        {"term": "Zone", "def": "A deployment area within a region (Think: Data Center Building)."},
        {"term": "Multi-Region", "def": "Redundancy across large distances (e.g., US-East + US-West). Survivors disaster."},
        {"term": "Org Policy", "def": "Guardrails that restrict WHAT resources can be created (e.g., No Public IPs)."},
        {"term": "Low Latency", "def": "Choosing a region close to your users to minimize speed."}
    ],
    "section_3_gcp_billing.md": [
        {"term": "Billing Account", "def": "Pays for the resources. Linked to a Credit Card or Invoice."},
        {"term": "Project", "def": "The container that holds resources. Must be linked to a Billing Account."},
        {"term": "Budget Alert", "def": "Emails you when spending exceeds a threshold. Does NOT stop spending."},
        {"term": "Quota", "def": "Hard limit on resources (e.g., 5 VPCs) to prevent abuse/accidents."},
        {"term": "Free Tier", "def": "Always free usage limits (e.g., 30GB storage, 1 e2-micro VM)."}
    ],
    "section_4_compute_engine.md": [
        {"term": "E2/N2 Series", "def": "General Purpose VMs. Balanced reliability and price."},
        {"term": "Spot VM", "def": "Up to 91% discount, but can be pre-empted (stopped) by Google with 30s notice."},
        {"term": "Live Migration", "def": "Google moves your running VM to a new host during maintenance without reboot."},
        {"term": "Sole-Tenant Node", "def": "Renting the physical server. Used for Compliance or Licensing."},
        {"term": "MIG (Managed Instance Group)", "def": "A group of identical VMs that scale up/down automatically."}
    ],
    "section_5_storage_basics.md": [
        {"term": "Persistent Disk", "def": "Network storage (NAS). Reliable, durable, survives VM stops."},
        {"term": "Local SSD", "def": "Physically attached to the server. Fast but ephemeral (data dies with VM)."},
        {"term": "Balanced PD", "def": "Best price/performance for general workloads."},
        {"term": "Image", "def": "The OS + Software template used to boot a VM."},
        {"term": "Snapshot", "def": "Backup of a disk. Incremental (only saves changes)."}
    ],
    "section_6_cloud_storage.md": [
        {"term": "Bucket", "def": "Container for objects (files). Must have a globally unique name."},
        {"term": "Standard Class", "def": "Hot data. Access frequently. Best for serving web assets."},
        {"term": "Nearline", "def": "Data accessed < 1/month. 30-day min storage fee."},
        {"term": "Coldline", "def": "Data accessed < 1/quarter. 90-day min storage fee."},
        {"term": "Archive", "def": "Deep freeze backup. < 1/year. 365-day min storage fee."},
        {"term": "Signed URL", "def": "Temporary time-bound access key for a specific file."}
    ],
    "section_7_week_1_review.md": [
        {"term": "IaaS", "def": "Infrastructure as a Service (Compute Engine). You manage OS + App."},
        {"term": "PaaS", "def": "Platform as a Service (App Engine). You manage App only."},
        {"term": "SaaS", "def": "Software as a Service (Gmail, Drive). You manage nothing."},
        {"term": "OpEx", "def": "Operational Expenditure. Pay-as-you-go (Cloud Model)."},
        {"term": "CapEx", "def": "Capital Expenditure. Upfront hardware cost (On-Prem Model)."}
    ]
}

def inject_flashcards():
    base_dir = os.path.join("curriculum", "content")
    
    for filename, cards in FLASHCARDS_DATA.items():
        path = os.path.join(base_dir, filename)
        if not os.path.exists(path):
            print(f"Skipping {filename} (Not found)")
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "<!-- FLASHCARDS" in content:
            print(f"Skipping {filename} (Already has flashcards)")
            continue
            
        # Append Flashcards
        json_str = json.dumps(cards, indent=2)
        appendix = f"\n\n\n<!-- FLASHCARDS\n{json_str}\n-->"
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content + appendix)
            
        print(f"Injected {len(cards)} flashcards into {filename}")

if __name__ == "__main__":
    inject_flashcards()
