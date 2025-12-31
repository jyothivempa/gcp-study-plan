# SECTION 18: Data Protection & KMS

> **Official Doc Reference**: [Cloud KMS](https://cloud.google.com/kms/docs)

## 1️⃣ The Hierarchy of Encryption
Google encrypts **ALL** data at rest by default (using AES-256). You don't have to do anything.
However, for compliance (banks, healthcare), you might need more control.

| Level | Name | Description | Who holds the key? | Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1** | **Default Encryption** | Google generates and manages keys. | Google | 90% of workloads. |
| **Level 2** | **CMEK** (Customer-Managed) | You generate keys in Cloud KMS. Google requests access to them. | You (in KMS) | Regulatory compliance (HIPAA). |
| **Level 3** | **CSEK** (Customer-Supplied) | You keep keys on your laptop. You send data + key to Google to process. | You (On-Prem) | Paranoid Security / Nuclear secrets. |

## 2️⃣ Envelope Encryption (The "Key to the Key")
How does Google encrypt 1 Petabyte of data efficiently? It doesn't use the KMS key for the data.
It uses **Envelope Encryption**.

1.  **DEK (Data Encryption Key):** A local key that encrypts the actual file (Chunk of data).
2.  **KEK (Key Encryption Key):** The master key in Cloud KMS that encrypts the DEK.

```mermaid
graph TD
    Data[Raw Data] -->|Encrypted by| DEK[Data Encryption Key]
    DEK -->|Encrypted by| KEK[Key Encryption Key (KMS)]
    KEK -->|Stored in| KMS[Cloud KMS]
```
*   **Performance:** KMS is only called *once* to decrypt the DEK. The DEK decrypts the data locally (fast).

## 3️⃣ Security Hardware (HSM)
*   **Software Keys:** Stored in Google's general crypto hardware.
*   **Cloud HSM:** Stored in a FIPS 140-2 Level 3 certified physical hardware device. Keys *never* leave the device.
*   **External Key Manager (EKM):** Keys are stored outside Google (e.g., in Thales on-prem).

## 4️⃣ Hands-On Lab: Creating a CMEK Bucket 🔐
**Mission:** Create a storage bucket that encrypts data using a key you control.

1.  **Create KeyRing & Key:**
    ```bash
    gcloud kms keyrings create my-ring --location global
    gcloud kms keys create my-key --keyring my-ring --location global --purpose encryption
    ```
2.  **Grant Access:** The Storage Service Account needs access to your key.
    ```bash
    gcloud kms keys add-iam-policy-binding my-key \
      --keyring my-ring --location global \
      --member serviceAccount:service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com \
      --role roles/cloudkms.cryptoKeyEncrypterDecrypter
    ```
3.  **Create Bucket:**
    ```bash
    gcloud storage buckets create gs://my-secret-bucket --default-encryption-key=projects/PROJECT/locations/global/keyRings/my-ring/cryptoKeys/my-key
    ```
4.  **Verify:** Upload a file. Check "Encryption details" in the console. It will say "Cloud KMS key".

## 5️⃣ Checkpoint Questions
1.  **Which encryption method requires you to upload the key with every API request?**
    *   *Answer: CSEK (Customer-Supplied).*
2.  **Why use Envelope Encryption?**
    *   *Answer: Performance. Encrypting large data with a remote KMS key is too slow.*
3.  **What happens to your data if you disable or destroy the Cloud KMS key (CMEK)?**
    *   *Answer: The data is "Crypto-Shredded". It becomes unreadable forever.*
