# Production-Ready Checklists

This document contains production deployment checklists for each major GCP service. Use these before deploying to production environments.

---

## ☑️ Compute Engine Production Checklist

### Before Launch
- [ ] **Machine Type:** Right-sized for workload (not over-provisioned)
- [ ] **Disk Type:** SSD for database/high-IOPS workloads
- [ ] **Preemptibility:** Only for fault-tolerant batch jobs
- [ ] **Instance Template:** Created for reproducibility
- [ ] **Startup Script:** Tested independently
- [ ] **Service Account:** Custom SA with least-privilege (not default)
- [ ] **Scopes:** Specific scopes, not `cloud-platform`
- [ ] **Labels:** Applied for cost tracking
- [ ] **Metadata:** SSH keys removed (use OS Login)

### Security
- [ ] **No Public IP:** Unless absolutely required
- [ ] **Firewall Rules:** Service account-based, not tag-based
- [ ] **OS Patch Management:** Enabled OS Config agent
- [ ] **Shielded VM:** Enabled for compliance workloads
- [ ] **Serial Console:** Disabled in production

### High Availability
- [ ] **Regional MIG:** For multi-zone redundancy
- [ ] **Health Checks:** Configured with proper thresholds
- [ ] **Auto-Healing:** Enabled with realistic initial delay
- [ ] **Auto-Scaling:** Based on actual metrics (CPU/custom)
- [ ] **Load Balancer:** Configured for distribution

### Monitoring
- [ ] **Ops Agent:** Installed for enhanced metrics
- [ ] **Log Aggregation:** Logs sent to Cloud Logging
- [ ] **Alerting:** Set up for CPU, disk, network
- [ ] **Uptime Checks:** Configured

---

## ☑️ Cloud Storage Production Checklist

### Before Launch
- [ ] **Bucket Naming:** Follows DNS naming convention
- [ ] **Location:** Multi-region for HA, regional for cost
- [ ] **Storage Class:** Matches access pattern
- [ ] **Uniform Access:** Enabled (bucket-only IAM)
- [ ] **Public Access Prevention:** Enabled unless public website

### Security
- [ ] **IAM Roles:** Least-privilege (not `allUsers`)
- [ ] **Signed URLs:** For temporary access
- [ ] **Encryption:** CMEK for sensitive data
- [ ] **Retention Policy:** Set for compliance
- [ ] **Object Versioning:** Enabled for critical data

### Cost Optimization
- [ ] **Lifecycle Rules:** Transition to Nearline/Coldline/Archive
- [ ] **Autoclass:** Enabled for automatic class transitions
- [ ] **Deletion Rules:** Auto-delete temporary files

### Monitoring
- [ ] **Audit Logs:** Admin/Data Access enabled
- [ ] **Metrics:** Monitoring bucket size & request count
- [ ] **Alerting:** Set up for unusually high costs

---

## ☑️ Cloud Run Production Checklist

### Before Launch
- [ ] **Container Image:** Built with distroless/alpine base
- [ ] **Min Instances:** ≥1 for latency-critical apps
- [ ] **Max Instances:** Set to prevent cost overrun
- [ ] **CPU Allocation:** "Always allocated" for background tasks
- [ ] **Memory:** Right-sized (512MB-2GB typical)
- [ ] **Request Timeout:** Realistic for workload
- [ ] **Concurrency:** Tuned (80 default, 1 for stateful)

### Security
- [ ] **IAM:** Not `allUsers` unless public API
- [ ] **Service Account:** Custom SA with minimal permissions
- [ ] **Secrets:** Stored in Secret Manager, not env vars
- [ ] **VPC Connector:** For private DB/service access
- [ ] **Ingress:** Internal-only if not public-facing

### Reliability
- [ ] **Health Checks:** /health endpoint implemented
- [ ] **Graceful Shutdown:** SIGTERM handled properly
- [ ] **Connection Pooling:** For database connections
- [ ] **Retry Logic:** Exponential backoff for external calls
- [ ] **Circuit Breaker:** For failing dependencies

### Monitoring
- [ ] **Structured Logging:** JSON format
- [ ] **Error Reporting:** Exceptions sent automatically
- [ ] **Trace:** Enabled for latency debugging
- [ ] **Custom Metrics:** Business metrics exported

---

## ☑️ Cloud SQL Production Checklist

### Before Launch
- [ ] **Instance Tier:** Sized for peak load
- [ ] **High Availability:** HA configured (failover)
- [ ] **Region:** Same as app for latency
- [ ] **Private IP:** Enabled for security
- [ ] **No Public IP:** Unless absolutely required
- [ ] **Maintenance Window:** Set to low-traffic hours

### Security
- [ ] **SSL/TLS:** Required for connections
- [ ] **Authorized Networks:** Minimal (prefer Cloud SQL Proxy)
- [ ] **IAM Database Auth:** Enabled
- [ ] **Encryption:** CMEK for compliance
- [ ] **Backup Encryption:** Enabled

### Backup & Recovery
- [ ] **Automated Backups:** Enabled (7-365 days)
- [ ] **Point-in-Time Recovery:** Enabled for MySQL/PostgreSQL
- [ ] **Backup Location:** Multi-region for disaster recovery
- [ ] **Backup Testing:** Restore tested quarterly

### Performance
- [ ] **Read Replicas:** For read-heavy workloads
- [ ] **Connection Pooling:** App-side or Cloud SQL Proxy
- [ ] **Query Insights:** Enabled for slow query detection
- [ ] **Database Flags:** Tuned for workload

### Monitoring
- [ ] **Uptime Checks:** For database connectivity
- [ ] **Alerting:** CPU, memory, storage capacity
- [ ] **Log Export:** To Cloud Logging/BigQuery
- [ ] **Performance Dashboard:** Created in Monitoring

---

## ☑️ VPC Network Production Checklist

### Before Launch
- [ ] **Custom VPC:** Not auto-mode
- [ ] **Subnet Sizing:** Right-sized CIDR blocks
- [ ] **IP Range Planning:** No overlap with on-prem
- [ ] **Regional Subnets:** Not global (for isolation)
- [ ] **Private Google Access:** Enabled for private VMs

### Security
- [ ] **Firewall Rules:** Service account-based
- [ ] **Default Deny:** All ingress denied except allowed
- [ ] **No 0.0.0.0/0:** Except load balancer health checks
- [ ] **IAP for SSH:** No TCP:22 from internet
- [ ] **VPC Flow Logs:** Enabled for compliance

### Connectivity
- [ ] **Cloud NAT:** For private VMs internet access
- [ ] **Cloud VPN/Interconnect:** For hybrid cloud
- [ ] **VPC Peering:** For cross-project access
- [ ] **Shared VPC:** For org-wide connectivity

### Monitoring
- [ ] **Flow Logs:** Exported to BigQuery
- [ ] **Firewall Rules Logging:** Enabled
- [ ] **Packet Mirroring:** For security analysis (if needed)
- [ ] **Network Intelligence:** Checked for topology

---

## ☑️ IAM Production Checklist

### Before Launch
- [ ] **No Owner Role:** In production projects
- [ ] **No Editor Role:** Too permissive
- [ ] **Predefined Roles:** Used instead of primitive
- [ ] **Custom Roles:** For fine-grained access
- [ ] **Service Accounts:** Per service, not per user
- [ ] **Groups:** Used for user management

### Security
- [ ] **No JSON Keys:** Use Workload Identity Federation
- [ ] **Key Rotation:** Automated for any keys
- [ ] **Least Privilege:** Minimal roles assigned
- [ ] **IAM Conditions:** Time/IP/resource-based
- [ ] **Organization Policies:** Domain restriction enabled

### Audit
- [ ] **Admin Activity Logs:** Always enabled (default)
- [ ] **Data Access Logs:** Enabled for sensitive data
- [ ] **Log Sinks:** Exported to SIEM
- [ ] **IAM Recommender:** Reviewed quarterly
- [ ] **Policy Analyzer:** Checked for over-permissions

---

## ☑️ GKE Production Checklist

### Before Launch
- [ ] **Autopilot vs Standard:** Decision documented
- [ ] **Regional Cluster:** For high availability
- [ ] **Release Channel:** Stable or Regular (not Rapid)
- [ ] **Workload Identity:** Enabled (not metadata server)
- [ ] **Binary Authorization:** For container security
- [ ] **Private Cluster:** Enabled

### Security
- [ ] **Shielded Nodes:** Enabled
- [ ] **Network Policy:** Enabled
- [ ] **Pod Security Standards:** enforced
- [ ] **RBAC:** Configured with least-privilege
- [ ] **Secret Management:** External Secrets Operator

### Reliability
- [ ] **Node Auto-Repair:** Enabled
- [ ] **Node Auto-Upgrade:** Enabled (maintenance window set)
- [ ] **Pod Disruption Budgets:** Configured
- [ ] **Horizontal Pod Autoscaler:** Configured
- [ ] **Liveness/Readiness Probes:** All pods have them

### Monitoring
- [ ] **GKE Monitoring:** Enabled
- [ ] **Workload Metrics:** Configured
- [ ] **Logging:** Structured JSON format
- [ ] **Alerting:** For pod crashes, node issues

---

## ☑️ BigQuery Production Checklist

### Before Launch
- [ ] **Dataset Location:** Matches data residency requirements
- [ ] **Table Partitioning:** By date for time-series data
- [ ] **Clustering:** On frequently filtered columns
- [ ] **Expiration:** Set for temp tables
- [ ] **Authorized Views:** For row-level security

### Cost Control
- [ ] **Query Cost Estimate:** Used before running
- [ ] **Maximum Bytes Billed:** Set on queries
- [ ] **BI Engine:** Enabled for dashboards
- [ ] **Slot Reservations:** For predictable costs >$10k/month
- [ ] **Cost Monitoring:** Alerts set for unusual spend

### Security
- [ ] **Column-Level Security:** For PII data
- [ ] **Data Masking:** For sensitive fields
- [ ] **Encryption:** CMEK for compliance
- [ ] **Audit Logs:** Data Access enabled
- [ ] **VPC Service Controls:** For data exfiltration prevention

### Performance
- [ ] **Avoid SELECT *:** Only query needed columns
- [ ] **Use Clustering:** For filter/aggregate queries
- [ ] **Approximate Aggregation:** For huge datasets
- [ ] **Materialized Views:** For repeated queries
- [ ] **INFORMATION_SCHEMA:** Checked for expensive queries

---

## 📝 Using These Checklists

### When to Use
- **Pre-Deployment Review:** Week before go-live
- **Security Audit:** Quarterly
- **Incident Postmortem:** After outages
- **Compliance:** Before audits

### How to Track
```bash
# Create a checklist issue in GitHub
gh issue create --title "Production Checklist: Cloud Run Service" --body "$(cat checklist.md)"

# Or use project management tools
# Jira, Asana, Monday.com, etc.
```

### Automation Tips
Many checklist items can be automated with:
- **Terraform:** Enforce configurations
- **Sentinel/OPA:** Policy as code
- **Cloud Build:** Pre-deployment checks
- **Config Connector:** Kubernetes-style management
