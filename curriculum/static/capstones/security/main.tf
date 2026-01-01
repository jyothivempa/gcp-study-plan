# Day 32: Security Capstone - IAM Least Privilege
# "The Auditor": This Terraform code creates a secure custom role and service account.

# 1. Custom Role (Least Privilege)
resource "google_project_iam_custom_role" "auditor_role" {
  role_id     = "app_auditor"
  title       = "App Auditor"
  description = "Can view logs and monitoring, but cannot edit resources."
  permissions = [
    "logging.logEntries.list",
    "logging.logs.list",
    "monitoring.timeSeries.list",
    "compute.instances.get",
    "compute.instances.list"
  ]
}

# 2. Service Account for the Application (Identity)
resource "google_service_account" "app_sa" {
  account_id   = "sa-app-prod"
  display_name = "Production Application Service Account"
}

# 3. Bind Role to Service Account (The "Link")
resource "google_project_iam_binding" "app_permissions" {
  project = "your-project-id"
  role    = google_project_iam_custom_role.auditor_role.name

  members = [
    "serviceAccount:${google_service_account.app_sa.email}",
  ]
}

# 4. (Bonus) Bind User to Group (Best Practice)
# resource "google_project_iam_binding" "dev_team" {
#   role    = "roles/viewer"
#   members = ["group:developers@example.com"]
# }
