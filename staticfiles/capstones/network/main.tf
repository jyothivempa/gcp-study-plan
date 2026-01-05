# Day 31: Network Capstone - Production VPC
# "The Fix": This Terraform code deploys the correct architecture.

provider "google" {
  project = "your-project-id"
  region  = "us-central1"
}

# 1. Custom VPC (No auto-subnets)
resource "google_compute_network" "prod_net" {
  name                    = "prod-net"
  auto_create_subnetworks = false
}

# 2. Private Subnet
resource "google_compute_subnetwork" "prod_subnet" {
  name          = "prod-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-central1"
  network       = google_compute_network.prod_net.id
}

# 3. Firewall: Allow Internal + HTTP from IAP/Lb
resource "google_compute_firewall" "allow_http" {
  name    = "allow-http-ingress"
  network = google_compute_network.prod_net.name

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  source_ranges = ["0.0.0.0/0"] # In production, restrict this!
  target_tags   = ["web-server"]
}

# 4. Cloud Router (Required for NAT)
resource "google_compute_router" "router" {
  name    = "prod-router"
  region  = google_compute_subnetwork.prod_subnet.region
  network = google_compute_network.prod_net.id
}

# 5. Cloud NAT (The Fix for Outbound Internet)
resource "google_compute_router_nat" "nat" {
  name                               = "prod-nat"
  router                             = google_compute_router.router.name
  region                             = google_compute_router.router.region
  nat_ip_allocate_option             = "AUTO_ONLY"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
}

# 6. The Web Server (Private IP only)
resource "google_compute_instance" "web_server" {
  name         = "web-server"
  machine_type = "e2-micro"
  zone         = "us-central1-a"
  tags         = ["web-server"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network    = google_compute_network.prod_net.id
    subnetwork = google_compute_subnetwork.prod_subnet.id
    # No access_config block = No Public IP
  }

  metadata_startup_script = "apt-get update && apt-get install -y nginx"
}
