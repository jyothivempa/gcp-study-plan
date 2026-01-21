import os
import re

CONTENT_DIR = r"d:\GCP\gcp-study-plan\curriculum\content"

def check_files():
    print(f"Scanning {CONTENT_DIR}...")
    
    issues = []
    
    # Files expected to have "Industry Context"
    enhanced_modules = [
        "section_6_iam_identity.md",
        "section_5_vpc_networking.md",
        "section_4_compute_engine.md",
        "section_15_containers.md",
        "section_16_kubernetes_arch.md",
        "section_23_cloud_functions.md",
        "section_6_cloud_storage.md",
        "section_11_storage_advanced.md",
        "section_8_instance_groups.md",
        "section_12_app_engine.md",
        "section_22_cloud_ops.md",
        "section_26_infrastructure_as_code_terraform.md",
        "section_27_cloud_build_ci_cd.md",
        "section_31_pubsub.md",
        "section_14_hybrid_connectivity.md",
        "section_18_kms_encryption.md",
        "section_24_bigquery_data_warehousing.md"
    ]

    for filename in os.listdir(CONTENT_DIR):
        if not filename.endswith(".md"):
            continue
            
        filepath = os.path.join(CONTENT_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check 1: Industry Context in enhanced modules
        if filename in enhanced_modules:
            if "Industry Context" not in content and "Industry Context:" not in content:
                 issues.append(f"[MISSING CONTENT] {filename} missing 'Industry Context' section")

        # Check 2: Broken local links (simple regex for [text](path))
        links = re.findall(r'\[.*?\]\((.*?)\)', content)
        for link in links:
            if link.startswith("http") or link.startswith("#") or link.startswith("mailto"):
                continue
            
            # Remove file:// prefix if present
            clean_link = link.replace("file:///", "").replace("file://", "")
            
            # Simple check for relative markdown links
            if clean_link.endswith(".md"):
                # Handle relative paths
                if "/" in clean_link or "\\" in clean_link:
                    # simplistic resolution
                    target_path = os.path.normpath(os.path.join(CONTENT_DIR, clean_link))
                else:
                    target_path = os.path.join(CONTENT_DIR, clean_link)
                
                if not os.path.exists(target_path):
                     # Try checking from root dir just in case
                     root_target = os.path.normpath(os.path.join(r"d:\GCP\gcp-study-plan", clean_link))
                     if not os.path.exists(root_target):
                        issues.append(f"[BROKEN LINK] {filename} -> {link}")

        # Check 3: Mermaid syntax markers
        if "```mermaid" in content:
            if "```" not in content.split("```mermaid")[1]:
                issues.append(f"[MERMAID ERROR] {filename} has unclosed mermaid block")

    if not issues:
        print("✅ No issues found in scanned files!")
    else:
        print(f"❌ Found {len(issues)} issues:")
        for issue in issues:
            print(issue)

if __name__ == "__main__":
    check_files()
