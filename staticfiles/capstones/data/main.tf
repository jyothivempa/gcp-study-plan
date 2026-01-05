# Day 34: Data Capstone - Analytics Pipeline
# "The Analyst": Terraform for BigQuery & Pub/Sub

provider "google" {
  project = "your-project-id"
  region  = "us-central1"
}

# 1. Pub/Sub Topic (Ingestion)
resource "google_pubsub_topic" "events_topic" {
  name = "ingestion-topic"
}

# 2. BigQuery Dataset
resource "google_bigquery_dataset" "analytics_ds" {
  dataset_id                  = "analytics_ds"
  friendly_name               = "Analytics Dataset"
  location                    = "US"
  default_table_expiration_ms = 3600000 # 1 Hour (Good for Cost Control!)
}

# 3. BigQuery Table (Schema)
resource "google_bigquery_table" "events_table" {
  dataset_id = google_bigquery_dataset.analytics_ds.dataset_id
  table_id   = "raw_events"

  schema = <<EOF
[
  {
    "name": "event_id",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "timestamp",
    "type": "TIMESTAMP",
    "mode": "REQUIRED"
  },
  {
    "name": "payload",
    "type": "JSON",
    "mode": "NULLABLE"
  }
]
EOF
}
