
import os
import pathlib
from django.core.management.base import BaseCommand
from curriculum.models import Week, Day

class Command(BaseCommand):
    help = 'Populates the database with the detailed 40-day GCP curriculum'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting 40-Day curriculum population...')

        # Path Setup
        project_root = pathlib.Path(__file__).resolve().parent.parent.parent.parent
        base_path = project_root / 'curriculum' / 'content'
        labs_path = project_root / 'curriculum' / 'labs'

        # Lab Mapping (Keep existing, allow for new ones)
        lab_mapping = {
            4: 'lab_04_compute_web_server.md',
            8: 'lab_08_vpc_peering.md',
            11: 'lab_11_load_balancer.md',
            16: 'lab_14_iam_troubleshooting.md', # Shifted Day
            27: 'lab_18_gke_deployment.md', # Shifted Day
            34: 'lab_26_terraform_basics.md' # Shifted Day
        }

        def get_hands_on_content(day_num):
            if day_num in lab_mapping:
                filename = lab_mapping[day_num]
                try:
                    with open(os.path.join(labs_path, filename), 'r', encoding='utf-8') as f:
                        return f.read()
                except FileNotFoundError:
                     return f"Lab file {filename} missing."
            return "Check the 'Console Walkthrough' section in the concept tab."

        def read_file(filename):
            try:
                # Try generic path first
                file_path = base_path / filename
                if not file_path.exists():
                     # Fallback for old named files if we don't rename them yet
                     # Ideally we just create new files strictly.
                     pass
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            except FileNotFoundError:
                return f"Content for {filename} not found. Please run content generation."

        # ---------------------------------------------------------
        # WEEK 1: Foundations & Compute (Days 1-7)
        # ---------------------------------------------------------
        week1, _ = Week.objects.get_or_create(number=1, defaults={'description': 'Cloud Computing Foundations & Compute'})
        days_w1 = [
            (1, 'What is Cloud Computing?', 'section_1_cloud_foundations.md'),
            (2, 'GCP Structure (Regions & Zones)', 'section_2_gcp_structure.md'),
            (3, 'Billing & Limits', 'section_3_gcp_billing.md'),
            (4, 'Compute Engine (VMs) Fundamentals', 'section_4_compute_engine.md'),
            (5, 'Disks (Persistent vs Local SSD)', 'section_5_storage_basics.md'),
            (6, 'Cloud Storage (Buckets & Lifecycle)', 'section_6_cloud_storage.md'),
            (7, 'Week 1 Review & Mini Mock', 'section_7_week_1_review.md'),
        ]

        # ---------------------------------------------------------
        # WEEK 2: Networking Deep Dive (Days 8-14)
        # ---------------------------------------------------------
        # Expanded Networking
        week2, _ = Week.objects.get_or_create(number=2, defaults={'description': 'Deep Dive: Networking'})
        days_w2 = [
            (8, 'VPC Networking Basics', 'section_8_vpc_basics.md'),
            (9, 'Subnets & IP Addressing', 'section_9_subnets_ip.md'),
            (10, 'Firewall Rules & Policies', 'section_10_firewall_rules.md'),
            (11, 'Load Balancing (Global vs Regional)', 'section_11_load_balancing.md'),
            (12, 'Cloud NAT & Cloud Router', 'section_12_cloud_nat_routes.md'),
            
            # NEW CONTENT
            # NEW CONTENT
            (13, 'Cloud DNS & Cloud CDN', 'section_13_dns_cdn.md'),
            (14, 'Project: Global Load Balancer', 'section_14_hybrid_connectivity.md'),
        ]

        # ---------------------------------------------------------
        # WEEK 3: Security & Identity (Days 15-21)
        # ---------------------------------------------------------
        # Expanded Security
        week3, _ = Week.objects.get_or_create(number=3, defaults={'description': 'Identity, Security & Operations'})
        days_w3 = [
            (15, 'IAM Fundamentals (Principals & Roles)', 'section_12_iam_core.md'), # Reusing file, shifted mapping
            (16, 'Service Accounts & Best Practices', 'section_13_service_accounts.md'),
            
            # NEW CONTENT
            (17, 'Advanced IAM: Workload Identity & Conditions', 'section_17_advanced_iam.md'),
            (18, 'Data Protection: KMS & Encryption', 'section_18_kms_encryption.md'),
            
            (19, 'Logging & Monitoring (Cloud Ops)', 'section_14_logging_monitoring.md'),
            (20, 'Security Command Center & DLP', 'section_20_security_operations.md'), # NEW
            (21, 'Project: The Automated Auditor', 'section_15_cloud_shell.md'),
        ]

        # ---------------------------------------------------------
        # WEEK 4: Serverless & Containers (Days 22-28)
        # ---------------------------------------------------------
        week4, _ = Week.objects.get_or_create(number=4, defaults={'description': 'Serverless & Kubernetes'})
        days_w4 = [
            (22, 'App Engine (Standard vs Flexible)', 'section_16_app_engine.md'),
            (23, 'Cloud Run Services', 'section_17_cloud_run.md'),
            
            # NEW CONTENT
            (24, 'Cloud Functions & Eventarc', 'section_24_functions_eventarc.md'),
            
            (25, 'GKE: Cluster Architecture', 'section_18_gke_basics.md'),
            # NEW CONTENT
            (26, 'GKE: Advanced Networking & Security', 'section_26_gke_advanced.md'),
            
            (27, 'Terraform (IaC) Fundamentals', 'section_26_infrastructure_as_code_terraform.md'),
            (28, 'Project: Event-Driven Serverless', 'section_27_cloud_build_ci_cd.md'),
        ]

        # ---------------------------------------------------------
        # WEEK 5: Data, ML & Databases (Days 29-35)
        # ---------------------------------------------------------
        week5, _ = Week.objects.get_or_create(number=5, defaults={'description': 'Databases, Data Analytics & AI'})
        days_w5 = [
            (29, 'Cloud SQL & AlloyDB', 'section_19_cloud_sql.md'),
            (30, 'Spanner & Bigtable', 'section_23_cloud_spanner_bigtable.md'),
            
            (31, 'BigQuery Fundamentals', 'section_24_bigquery_data_warehousing.md'),
            # NEW
            (32, 'Data Pipelines: Dataflow vs Dataproc', 'section_32_dataflow_dataproc.md'),
            (33, 'Pub/Sub Messaging', 'section_25_pub_sub_data_pipelines.md'),
            
            # NEW
            (34, 'Vertex AI & Machine Learning Basics', 'section_34_vertex_ai.md'),
            (35, 'Database Migration Strategy', 'section_35_db_migration.md'),
        ]

        # ---------------------------------------------------------
        # WEEK 6: Reliability & Certification (Days 36-40)
        # ---------------------------------------------------------
        week6, _ = Week.objects.get_or_create(number=6, defaults={'description': 'Reliability, Architecture & Final Exam'})
        days_w6 = [
             # NEW
            (36, 'SRE Principles & Cloud Operations', 'section_36_sre_ops.md'),
             # NEW
            (37, 'Cost Management & Optimization (FinOps)', 'section_37_finops.md'),
            
            (38, 'Compliance & Security Requirements', 'section_28_security_compliance.md'),
            (39, 'Architect Case Studies', 'section_29_architect_case_studies.md'),
            (40, 'Final Exam Readiness', 'section_30_final_exam_readiness.md'),
            (41, 'Bonus Mock Exam - Part 2', 'section_30_final_exam_readiness.md'), # Re-using file for now, content differs in quiz
        ]

        # ---------------------------------------------------------
        # WEEK 7: CAPSTONE LABORATORY (Days 42-45)
        # ---------------------------------------------------------
        week7, _ = Week.objects.get_or_create(number=7, defaults={'description': 'Applied Capstone Projects'})
        days_w7 = [
            (42, 'Project: Networking Detective', 'section_31_network_capstone.md'),
            (43, 'Project: Security Audit', 'section_32_security_capstone.md'),
            (44, 'Project: Automated DevOps Pipeline', 'section_33_devops_capstone.md'),
            (45, 'Project: Big Data Analytics', 'section_34_data_capstone.md'),
        ]

        # ---------------------------------------------------------
        # POPULATION LOOP
        # ---------------------------------------------------------
        all_weeks = [
            (week1, days_w1), 
            (week2, days_w2), 
            (week3, days_w3), 
            (week4, days_w4), 
            (week5, days_w5), 
            (week6, days_w6),
            (week7, days_w7)
        ]

        for week_obj, days_list in all_weeks:
            for day_num, title, filename in days_list:
                content = read_file(filename)
                
                parts = content.split('## 7️⃣ Checkpoint Questions')
                if len(parts) < 2:
                     parts = content.split('## Checkpoint Questions')
                
                # Check for "Mini Mock Exam" style separator if standard one fails
                if len(parts) < 2:
                    parts = content.split('## 📝 Mini Mock Exam')
                
                concept = parts[0]
                quiz = parts[1] if len(parts) > 1 else "No quiz generated."

                Day.objects.update_or_create(
                    number=day_num,
                    defaults={
                        'week': week_obj,
                        'title': title,
                        'description': f"Day {day_num}: {title}",
                        'concept_content': concept,
                        'hands_on_content': get_hands_on_content(day_num),
                        'interview_questions': quiz,
                        'outcome': "Mastering GCP one day at a time.",
                    }
                )
                self.stdout.write(self.style.SUCCESS(f'Updated Day {day_num}: {title}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated FULL 40-Day Curriculum'))
