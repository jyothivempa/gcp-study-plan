
import os
import re

# Base content directory
CONTENT_DIR = r"d:\ultimateCode\gcp_study_plan\curriculum\content"

# Standard template for a lesson
TEMPLATE = """# Day {day}: {title}

## Learning Objectives
By the end of this day, you should be able to:
- Understand the core concepts of {topic}.
- Identify when to use {topic} in an enterprise architecture.
- configure basic settings for {topic} in the Google Cloud Console.

## 1. Core Concepts

### What is {topic}?
*Detailed explanation goes here matching the specific topic.*

[Mermaid Diagram Placeholder]

### Key Features
- **Feature 1**: ...
- **Feature 2**: ...
- **Feature 3**: ...

## 2. Real-World Analogy
**The Scenario**: Imagine you are building...
*Analogy text.*

## 3. Architecture Patterns
How does {topic} fit into a larger system?
- **Pattern A**: ...
- **Pattern B**: ...

## 4. Cheat Sheet & Exam Tips
> [!TIP]
> **Exam Watch**: Look for keywords like "global", "managed", or "compliant" when seeing questions about {topic}.

## 5. Hands-on Lab
**Objective**: Set up a basic {topic} instance.
1. Go to Console > {topic}.
2. Click Create...

## 6. Daily Quiz
1. **Question 1**: What is the primary use case for {topic}?
   - A) Wrong answer
   - B) Correct answer
   - C) Wrong answer
   - D) Wrong answer
   > **Correct**: B) ...

"""

# Map of missing or collision days to generate/fix
# We will focus on filling 23-30 and re-aligning 12+ if needed.
# Current list had collision at 12. Let's assume we map explicitly for safety.

days_to_create = {
    23: ("Cloud Spanner & Bigtable", "Global, horizontally scalable managed databases."),
    24: ("BigQuery & Data Warehousing", "Serverless, highly scalable, and cost-effective multi-cloud data warehouse."),
    25: ("Pub/Sub & Data Pipelines", "Ingestion and messaging middleware for streaming analytics."),
    26: ("Infrastructure as Code (Terraform)", "Managing GCP resources declaratively using Terraform."),
    27: ("Cloud Build & CI/CD", "Automating the delivery of your software."),
    28: ("Security & Compliance", "Cloud Armor, KMS, and Security Command Center."),
    29: ("Architect Case Studies", "Analyzing Mountkirk Games, TerramEarth, and EHR Healthcare."),
    30: ("Final Exam Readiness", "Mock exam strategy and final review.")
}

def create_missing_files():
    if not os.path.exists(CONTENT_DIR):
        print(f"Directory not found: {CONTENT_DIR}")
        return

    for day, (title, topic) in days_to_create.items():
        filename = f"section_{day}_{title.lower().replace(' & ', '_').replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_')}.md"
        filepath = os.path.join(CONTENT_DIR, filename)
        
        if os.path.exists(filepath):
            print(f"Day {day} already exists at {filename}, skipping.")
            continue
            
        content = TEMPLATE.format(day=day, title=title, topic=topic)
        
        # Customize specific fields slightly for better start
        if day == 26:
            content = content.replace("[Mermaid Diagram Placeholder]", "```mermaid\ngraph LR\n    A[Code Change] -->|Push| B(Repo)\n    B -->|Trigger| C{Cloud Build}\n    C -->|Plan/Apply| D[GCP Infrastructure]\n```")
        elif day == 29:
            content = content.replace("## 1. Core Concepts", "## 1. The Case Studies").replace("### What is Architect Case Studies?", "### Analyzing The Official Case Studies")
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created Day {day}: {filename}")

if __name__ == "__main__":
    create_missing_files()
