from django.core.management.base import BaseCommand
from curriculum.models import Day, QuizQuestion

class Command(BaseCommand):
    help = 'Distributes Q16-Q60 to their respective days based on topic.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Mapping questions to days...')
        
        # Mapping: Question Data -> Day Number
        # Helper to simplify data entry
        def q(day, text, correct_idx, opts):
            return {
                "day": day,
                "text": text,
                "options": opts,
                "correct": correct_idx
            }

        questions = [
            q(10, "Scenario: Two firewall rules exist: Rule A (1000, allow tcp:443), Rule B (500, deny all). Traffic blocked. Why?", 2, ["Allow overrides deny", "Lower priority (500) wins", "Random evaluation", "HTTPS needs LB"]),
            q(8, "Scenario: Multiple projects need shared subnets but isolated IAM and billing. BEST solution?", 3, ["VPC Peering", "VPN", "Shared VPC", "Interconnect"]),
            q(17, "Scenario: A contractor needs access to a bucket only during business hours.", 3, ["Custom role", "Signed URLs", "IAM Conditions", "ACLs"]),
            q(9, "Scenario: VMs without public IPs need access to Google APIs only, not the internet.", 3, ["Cloud NAT", "VPN", "Private Google Access", "Interconnect"]),
            q(19, "Scenario: Logs must be queried using SQL and retained long-term. Best export destination?", 2, ["Cloud Storage", "BigQuery", "Error Reporting", "Monitoring"]),
            q(3, "Scenario: Finance wants spending to stop automatically at ₹50,000.", 3, ["Budget", "Billing export", "Quota", "Alerting policy"]),
            q(5, "Scenario: Multiple VMs need shared POSIX-compliant storage.", 3, ["Persistent Disk", "Cloud Storage", "Filestore", "Bigtable"]),
            q(25, "Scenario: A GKE cluster runs out of nodes during peak load. What should be enabled?", 2, ["Horizontal Pod Autoscaler", "Cluster Autoscaler", "Load Balancer", "Node taints"]),
            q(11, "Scenario: Traffic reaches a VM, but the load balancer marks it unhealthy. Most likely issue?", 1, ["Firewall blocking health check IPs", "IAM permission issue", "Disk full", "Wrong VM size"]),
            q(4, "Scenario: A service account has correct IAM role but still fails API calls. Likely cause?", 1, ["Missing OAuth scope", "Wrong project", "Firewall issue", "Disk quota"]),
            q(15, "Scenario: A VM in Project A must access Cloud Storage in Project B. What is REQUIRED?", 2, ["VPC peering", "Cross-project IAM binding", "Shared VPC", "VPN"]),
            q(6, "Scenario: Data must be accessible worldwide with lowest latency. Which storage class?", 4, ["Regional", "Nearline", "Coldline", "Multi-region"]),
            q(4, "Scenario: You need to recreate many identical VMs quickly. What should you use?", 2, ["Snapshot", "Image", "Disk clone", "Startup script"]),
            q(11, "Scenario: An internal app should not be accessible from the internet. Which load balancer?", 3, ["External HTTPS", "Network LB", "Internal TCP/UDP", "External TCP"]),
            q(15, "Scenario: Admins want identity-based access instead of network-based. What should be used?", 3, ["VPN", "Firewall", "Cloud IAP", "NAT"]),
            q(30, "Scenario: You need millisecond latency key-value storage at petabyte scale. Which database?", 3, ["Firestore", "Cloud SQL", "Bigtable", "Spanner"]),
            q(4, "Scenario: VM costs reduce automatically without commitment. Which discount applies?", 2, ["Committed use", "Sustained use", "Preemptible", "Free tier"]),
            q(4, "Scenario: Your preemptible VM was terminated. What should your app do?", 2, ["Ignore", "Retry from checkpoint", "Increase VM size", "Disable preemption"]),
            q(17, "Scenario: IAM permissions must never be granted accidentally. What prevents privilege escalation?", 2, ["Owner role", "Deny policies", "Editor role", "Viewer role"]),
            q(1, "Scenario: IAM set at folder level affects all projects below. What concept is tested?", 2, ["Billing inheritance", "Resource hierarchy", "Networking", "Quotas"]),
            q(19, "Scenario: You want an alert when uptime check fails. What is REQUIRED?", 3, ["Logging", "Monitoring metric", "Alerting policy", "Trace"]),
            q(19, "Scenario: You need to investigate application logs for errors. Which service?", 2, ["Monitoring", "Logging", "Trace", "Debugger"]),
            q(22, "Scenario: An App Engine Standard app hits scaling limits. What is the reason?", 1, ["Fixed instance types", "Language restrictions", "Cold starts", "Billing issue"]),
            q(23, "Scenario: A Cloud Run service is slow under load. What setting should be reviewed?", 1, ["Concurrency", "Disk size", "VPC peering", "NAT"]),
            q(25, "Scenario: Costs unexpectedly increase in GKE Autopilot. Why?", 2, ["Node overprovisioning", "You pay per pod resources", "Fixed pricing", "Free tier expired"]),
            q(2, "Scenario: An app must survive regional failure. Best design?", 3, ["Single region", "Multi-zone", "Multi-region", "Backup only"]),
            q(11, "Scenario: You need L7 routing for HTTPS traffic. Which LB?", 3, ["TCP LB", "Network LB", "HTTP(S) LB", "Internal TCP"]),
            q(6, "Scenario: Objects should move to cheaper storage after 30 days. What should you use?", 2, ["IAM", "Lifecycle rule", "Versioning", "Signed URL"]),
            q(6, "Scenario: Temporary access to a private object is required. What is best?", 3, ["Make bucket public", "ACL", "Signed URL", "Viewer role"]),
            q(23, "Scenario: A workload requires minimal ops and container support. Best option?", 3, ["GKE Standard", "Compute Engine", "Cloud Run", "App Engine Flexible"]),
            q(11, "Scenario: Developers should not manage SSL certificates. What should you use?", 2, ["Self-signed cert", "Managed SSL", "VPN cert", "IAM"]),
            q(4, "Scenario: VM deployments must be consistent and repeatable. What enables this?", 2, ["SSH", "Instance templates", "Startup scripts", "Snapshots"]),
            q(10, "Scenario: Firewall rules behave unexpectedly. What should you review?", 2, ["Creation time", "Priority", "Network tag name", "Region"]),
            q(19, "Scenario: Audit logs must cover all projects. Where configure?", 3, ["Project", "Folder", "Organization", "Resource"]),
            q(30, "Scenario: A relational DB must scale globally. Which service?", 4, ["Cloud SQL", "Firestore", "Bigtable", "Spanner"]),
            q(19, "Scenario: You need to debug production code without redeploying. Which tool?", 2, ["Logging", "Debugger", "Trace", "Monitoring"]),
            q(30, "Scenario: A service must meet very low RPO and RTO globally. Best database?", 4, ["Cloud SQL", "Firestore", "Bigtable", "Spanner"]),
            q(6, "Scenario: Objects were accidentally deleted. What prevents this?", 2, ["Lifecycle rules", "Versioning", "IAM Viewer", "Monitoring"]),
            q(6, "Scenario: A developer needs temporary upload access. What should be used?", 2, ["Owner role", "Signed URL", "Public bucket", "ACL"]),
            q(23, "Scenario: You want the LOWEST operational overhead compute. Which option?", 3, ["Compute Engine", "GKE", "Cloud Run", "VM MIG"]),
            q(15, "Scenario: A company requires separation of duties. Best IAM practice?", 3, ["Owner role", "Editor role", "Custom roles", "Shared accounts"]),
            q(19, "Scenario: Requests are slow and you need latency breakdown. Which tool?", 2, ["Logging", "Trace", "Monitoring", "Debugger"]),
            q(3, "Scenario: Costs spike due to runaway usage. What prevents this?", 2, ["Budget", "Quota", "IAM", "Logging"]),
            q(28, "Scenario: You want instant rollback deployment. Which strategy?", 3, ["Rolling", "Canary", "Blue/Green", "Recreate"]),
            q(1, "Scenario: Security governance must apply everywhere. Where manage IAM?", 4, ["Resource", "Project", "Folder", "Organization"]),
        ]

        added_count = 0
        for item in questions:
            try:
                day = Day.objects.get(number=item["day"])
                
                # Check duplication
                if not QuizQuestion.objects.filter(day=day, question_text=item["text"]).exists():
                    QuizQuestion.objects.create(
                        day=day,
                        question_text=item["text"],
                        option_1=item["options"][0],
                        option_2=item["options"][1],
                        option_3=item["options"][2],
                        option_4=item["options"][3],
                        correct_option=item["correct"]
                    )
                    added_count += 1
                else:
                    self.stdout.write(f'Skipped dup: {item["text"][:30]}...')

            except Day.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Day {item["day"]} not found. Skipping question.'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully distributed {added_count} Hard Questions across the curriculum.'))
