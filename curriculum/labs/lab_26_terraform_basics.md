
# 🛠️ Lab 26: Terraform Basics

**Objective:** Use Terraform to create a Cloud Storage bucket and a VM Instance as Code.
**Duration:** 20 Minutes

## 1. Setup Cloud Shell
Open Cloud Shell. It has Terraform pre-installed!
Create a directory for your project:

```bash
mkdir terraform-lab
cd terraform-lab
```

## 2. Create `main.tf`
Create the configuration file.
```bash
nano main.tf
```
Paste this content (Replace `YOUR_PROJECT_ID` with your actual ID):

```hcl
provider "google" {
  project = "YOUR_PROJECT_ID"
  region  = "us-central1"
  zone    = "us-central1-a"
}

# 1. Create a Bucket
resource "google_storage_bucket" "my_bucket" {
  name          = "tf-bucket-unique-${random_id.instance_id.hex}"
  location      = "US"
  force_destroy = true
}

# 2. Random ID generator (for unique names)
resource "random_id" "instance_id" {
  byte_length = 4
}

# 3. Create a VM
resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance"
  machine_type = "e2-micro"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {
      # Include this section to give the VM an external ip address
    }
  }
}
```

## 3. Initialize Terraform
Downloads the Google Provider plugins.
```bash
terraform init
```

## 4. Plan (Preview)
See what Terraform *wants* to do. It should say "Plan: 3 to add".
```bash
terraform plan
```

## 5. Apply (Execute)
Make it real. Type `yes` when prompted.
```bash
terraform apply
```

## 6. Verify
Check the console. You will see a new Bucket and a VM named `terraform-instance`.

## 🧹 Cleanup (Destroy)
The magic of Terraform: one command to clean up *everything*.
```bash
terraform destroy
```
(Type `yes` to confirm).
