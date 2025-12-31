
DAYS_CONTENT = {
    # WEEK 1: CLOUD FUNDAMENTALS & CORE INFRASTRUCTURE
    2: {
        "title": "Virtual Machines (Compute Engine)",
        "description": "Create your first Virtual Machine (VM).",
        "concept": """
### 1️⃣ Plain-English Explanation
Imagine you need a computer, but instead of going to Best Buy to buy a laptop, you click a button and Google rents you one of theirs for a few minutes. That is **Compute Engine**. It allows you to create and run **Virtual Machines (VMs)** on Google's infrastructure.

### 2️⃣ Real-World Analogy
*   **On-Premise (Own Laptop)**: You buy a car. You pay for gas, repairs, insurance, and parking. If it breaks, you fix it.
*   **Compute Engine (Cloud VM)**: You rent a Hertz rental car. You just pay for the miles/minutes you drive. If it breaks, Hertz gives you a new one.

### 3️⃣ Why This Exists (EXAM FOCUS)
*   **Flexibility**: You can have a super-computer (100 CPUs) for 1 hour to crunch data, then delete it.
*   **Migration**: It's the easiest way to move existing apps to the cloud (Lift and Shift).

### 4️⃣ Key Concepts
1.  **Machine Families**:
    *   **E2/N2 (General Purpose)**: The "Honda Civic". Balanced price/performance. Good for web servers.
    *   **C2 (Compute Optimized)**: The "Sports Car". Fast CPU. Good for gaming, video encoding.
    *   **M2 (Memory Optimized)**: The "Semi Truck". Huge RAM (up to 12TB). Good for massive databases (SAP HANA).
2.  **Disks**:
    *   **Persistent Disk (PD)**: Like a USB drive plugged in via network cable. Slows down if far away, but data is safe.
    *   **Local SSD**: Physically inside the server itself. Super fast, but if the VM stops, data is **lost** (Ephemeral).
3.  **Preemptible / Spot VMs**:
    *   Spare capacity Google sells at 90% discount.
    *   *Catch*: Google can turn them off with 30 seconds notice.
    *   *Use Case*: processing batch jobs that can restart.

### 6️⃣ Exam Triggers 🚨
*   **"Cost-Effective"**: Check if *Spot/Preemptible* VMs are an option.
*   **"High Performance DB"**: Look for *Local SSD* (for speed) or *Memory Optimized* family.
*   **"Web Server"**: *General Purpose* (E2) is usually the answer.

### 7️⃣ Comparison
| Feature | Persistent Disk (Standard) | Local SSD |
| :--- | :--- | :--- |
| **Speed** | Good | Insanely Fast |
| **Data Safety** | Durable (Safe) | Ephemeral (Lost on stop) |
| **Use Case** | Boot disk, File storage | Cache, Scratch data |

### 9️⃣ One-Line Memory Hook 🧠
**Compute Engine is just a rental computer that lives in Google's basement.**
""",
        "hands_on": """
### 5️⃣ Console Walkthrough (STEP-BY-STEP)

**Goal**: Launch a simple Web Server.

1.  **Navigate**: Go to **Compute Engine** > **VM Instances**.
    *   *Note*: If API is not enabled, click "Enable". usage starts billing only after creation.
2.  **Click**: **Create Instance**.
3.  **Configure**:
    *   **Name**: `web-server-1` (Must be lowercase).
    *   **Region**: `us-central1` (Iowa).
    *   **Zone**: `us-central1-a`.
    *   **Machine Type**: `e2-micro` (This is often free-tier eligible!).
4.  **Boot Disk**:
    *   Click "Change".
    *   Select **Debian** (Linux) or **Ubuntu**.
5.  **Firewall**:
    *   **IMPORTANT**: Check the box **"Allow HTTP traffic"**. This opens part of the force field so we can see the website.
6.  **Advanced Options** (The Magic Trick):
    *   Expand **Advanced Options** > **Management**.
    *   Find **Startup Script**. Paste this:
        ```bash
        #! /bin/bash
        apt-get update
        apt-get install -y nginx
        service nginx start
        sed -i -- 's/nginx/Google Cloud/g' /var/www/html/index.nginx-debian.html
        ```
    *   *Why?* This script runs automatically when the VM turns on. It installs a web server (Nginx).
7.  **Click Create**.
8.  **Verify**:
    *   Wait for the green checkmark.
    *   Click the **External IP** link.
    *   You should see "Welcome to Google Cloud!"
""",
        "outcome": "deployed a functional NGINX web server on a Virtual Machine.",
        "interview_qs": """
### 8️⃣ Interview-Ready Q&A
**Q1: What is the difference between specific machine families (E2 vs C2)?**
*Answer:* E2 is general purpose (balanced CPU/RAM) for standard apps. C2 is Compute Optimized for high-performance computing (like video rendering).

**Q2: When would you absolutely NOT use a Preemptible VM?**
*Answer:* For the database or the main login server. Anything that cannot handle a sudden shutdown.

**Q3: Does stopping a VM stop the billing?**
*Answer:* It stops billing for the *Compute* (CPU/RAM), but you still pay for the *Storage* (Boot Disk) unless you delete the instance.
"""
    },
    3: {
        "title": "Cloud Shell & gcloud CLI",
        "description": "Control the cloud from the command line.",
        "concept": """
### 1️⃣ Plain-English Explanation
The Google Cloud Console (the website) is great for beginners, but it's slow. If you need to create 50 VMs, clicking buttons takes forever.
The **CLI (Command Line Interface)** lets you type text commands to do things instantly. **Cloud Shell** is a computer-in-your-browser that comes pre-installed with all these tools.

### 2️⃣ Real-World Analogy
*   **Console (UI)**: Ordering food at a restaurant by pointing at pictures on the menu. Easy, but slow.
*   **gcloud (CLI)**: Being the head chef and shouting "Two Burgers, Now!". Fast, efficient, specific.

### 3️⃣ Why This Exists (EXAM FOCUS)
*   **Automation**: You can script commands.
*   **Speed**: Faster than UI.
*   **Zero Setup**: Cloud Shell starts in 5 seconds; no need to install Python/SDKs on your laptop.

### 4️⃣ Key Concepts
1.  **Cloud Shell**:
    *   It's a small Linux VM given to you for free (temporary).
    *   **5GB Persistent Storage**: Your home folder (`/home/user`) is saved. Everything else is wiped when you close the tab.
2.  **gcloud SDK**:
    *   The tool you type commands into. `gcloud compute...`, `gcloud storage...`.

### 6️⃣ Exam Triggers 🚨
*   **"Pre-installed tools"**: Cloud Shell has Terraform, Docker, Java, Python built-in.
*   **"Persist Files"**: Only your `$HOME` directory is saved.
*   **"Private Network Access"**: Cloud Shell CANNOT access your VPC (private VMs) by default unless configured.

### 9️⃣ One-Line Memory Hook 🧠
**Cloud Shell is your free admin laptop inside the web browser.**
""",
        "hands_on": """
### 5️⃣ Console Walkthrough (STEP-BY-STEP)

**Goal**: Create a VM without using the mouse.

1.  **Open Cloud Shell**:
    *   Look at the top right of the blue bar. Click the icon that looks like a terminal `>_`.
    *   Wait for "Provisioning...".
2.  **Authorize**:
    *   A popup will ask to Authorize. Click **Authorize**.
3.  **Command 1: Set Project**:
    ```bash
    gcloud config set project [YOUR_PROJECT_ID]
    ```
    *   *Tip*: Your Project ID is in the yellow box on the dashboard.
4.  **Command 2: List Zones**:
    ```bash
    gcloud compute zones list
    ```
5.  **Command 3: Create VM**:
    ```bash
    gcloud compute instances create command-line-vm --zone=us-central1-a --machine-type=e2-micro
    ```
6.  **Verify**:
    *   Go to **Compute Engine** UI page. Refresh. You will see `command-line-vm` there!
7.  **Cleanup**:
    ```bash
    gcloud compute instances delete command-line-vm --zone=us-central1-a --quiet
    ```
""",
        "outcome": "mastered the gcloud CLI and Cloud Shell environment.",
        "interview_qs": """
### 8️⃣ Interview Q&A
**Q1: Where is your Cloud Shell home directory stored?**
*Answer:* It is stored on a 5GB Persistent Disk that keeps your files safe even after the Cloud Shell session ends.

**Q2: Can I install my own tools in Cloud Shell?**
*Answer:* Yes (`sudo apt-get install`), but unless they are in your `$HOME` folder, they will disappear next time you restart Cloud Shell.
"""
    },
    4: {
        "title": "VPC Networking Fundamentals",
        "description": "The nervous system of the cloud: How computers talk to each other.",
        "concept": """
### 1️⃣ Plain-English Explanation
A **VPC (Virtual Private Cloud)** is your own private bubble inside Google's massive network. It's like having your own office building. Inside, you can put desks (VMs) and run cables (Subnets) however you want. Nobody from the outside can walk in unless you open the door.

### 2️⃣ Real-World Analogy
*   **VPC**: Your house. Secure, private walls.
*   **Subnet**: The rooms (Kitchen, Bedroom).
*   **Firewall**: The security guard at the door checking IDs.
*   **Routes**: The hallways and signs pointing where to go.

### 3️⃣ Why This Exists (EXAM FOCUS)
*   **Isolation**: Keep your databases safe from the public internet.
*   **Global Reach**: This is GCP's superpower. A Single VPC spans the **whole world**.

### 4️⃣ Key Concepts
1.  **VPC is Global**:
    *   Unlike AWS (where VPC is Regional), in GCP, one VPC covers Virginia, Tokyo, and London.
2.  **Subnets are Regional**:
    *   You carve out IP ranges in specific regions.
    *   `us-central1` gets `10.0.1.0/24`.
    *   `asia-east1` gets `10.0.2.0/24`.
3.  **Internal Communication**:
    *   VM in US can talk to VM in Asia via **Private IP** automatically over Google's fiber lines. Fast and secure.

### 6️⃣ Exam Triggers 🚨
*   **"Span multiple regions"**: The answer is always **VPC** (Global).
*   **"Span multiple zones"**: The answer is **Subnet** (Regional, covers all zones in that region).
*   **"Auto Mode vs Custom Mode"**:
    *   *Auto*: Google makes subnets for you (easy, but wasteful IPs).
    *   *Custom*: You choose IP ranges (Production Best Practice).

### 9️⃣ One-Line Memory Hook 🧠
**The VPC is the House (Global), Subnets are Rooms (Regional).**
""",
        "hands_on": """
### 5️⃣ Console Walkthrough (STEP-BY-STEP)

**Goal**: Build a Custom Network spanning two continents.

1.  **Navigate**: **VPC Network** > **VPC networks**.
2.  **Click**: **Create VPC Network**.
3.  **Name**: `global-corp-net`.
4.  **Subnet Creation Mode**: Choose **Custom**. (Important!)
5.  **Add Subnet 1 (USA)**:
    *   **Name**: `subnet-usa`
    *   **Region**: `us-central1`
    *   **Range**: `10.0.1.0/24` (256 addresses).
6.  **Add Subnet 2 (Europe)**:
    *   **Name**: `subnet-eu`
    *   **Region**: `europe-west1`
    *   **Range**: `10.0.2.0/24`.
7.  **Firewall Rules**:
    *   In the "Firewall rules" tab (inside the creation wizard), select `allow-ssh` (if available) or we will create it later.
8.  **Click Create**.
    *   *Result*: You now have a private network that exists in Iowa and Belgium simultaneously.
""",
        "outcome": "architected a global network with custom regional routing.",
        "interview_qs": """
### 8️⃣ Interview Q&A
**Q1: Is a Google VPC regional or global?**
*Answer:* Global. A single VPC can contain subnets in every GCP region.

**Q2: Can two subnets in the same VPC talk to each other?**
*Answer:* Yes, by default. All subnets in a VPC have a route to each other, even across regions.

**Q3: What is "Custom Mode" VPC?**
*Answer:* It allows you to manually define the CIDR ranges for your subnets, giving you full control over your network topology.
"""
    },
    5: {
        "title": "IP Addresses & Firewalls",
        "description": "Controlling who can access your VM.",
        "concept": """
### 1️⃣ Plain-English Explanation
Just because you have a network doesn't mean it's safe. **Firewalls** are the bouncers. They stare at every packet of data trying to enter your VM and check a list: "Are you allowed in?".
**IP Addresses** are the phone numbers. Internal IPs work inside the house. External IPs work on the public internet.

### 2️⃣ Real-World Analogy
*   **External IP**: Your public mailing address. Anyone can send junk mail here.
*   **Internal IP**: Your room number at a hotel. Only people inside the hotel can find you.
*   **Firewall**: The doorman. "No shirt, no shoes, no service."

### 3️⃣ Why This Exists (EXAM FOCUS)
*   **Security**: The #1 reason clouds are safe. Default is "Deny All".
*   **Stateful**: If you allow a request *in*, the response is automatically allowed *out*. You don't need two rules.

### 4️⃣ Key Concepts
1.  **Ingress vs Egress**:
    *   **Ingress**: Incoming traffic (Internet -> VM).
    *   **Egress**: Outgoing traffic (VM -> Internet).
2.  **Network Tags**:
    *   Instead of writing rules for IP addresses (messy), we put a sticky note (Tag) on a VM.
    *   *Rule*: "Allow port 80 for any VM with tag `web-server`".
    *   Now, whenever you create a web server, just give it that tag!

### 6️⃣ Exam Triggers 🚨
*   **"Stateful"**: Google Firewalls are stateful.
*   **"Tag based"**: The modern, scalable way to manage rules.
*   **"Priority"**: Lower number = Higher priority (1000 overrides 65534).

### 9️⃣ One-Line Memory Hook 🧠
**Firewalls block everything unless you explicitly poke a hole in the wall.**
""",
        "hands_on": """
### 5️⃣ Console Walkthrough (STEP-BY-STEP)

**Goal**: Open access to a Web Server using Tags.

1.  **Navigate**: **VPC Network** > **Firewall**.
2.  **Click**: **Create Firewall Rule**.
3.  **Configure**:
    *   **Name**: `allow-web-traffic`
    *   **Network**: `global-corp-net` (The one we made yesterday).
    *   **Direction**: Ingress (Inbound).
    *   **Action**: Allow.
    *   **Targets**: Specified target tags.
    *   **Target Tags**: Type `web-public`.
    *   **Source Filter**: IPv4 ranges.
    *   **Source Ranges**: `0.0.0.0/0` (This means "The Whole Internet").
    *   **Protocols/Ports**: Check `tcp` and type `80`.
4.  **Click Create**.
5.  **Apply it**:
    *   Go to **Compute Engine**. Edit a VM.
    *   Find **Network Tags**. Add `web-public`. Save.
    *   *Boom*: That VM is now accessible on port 80.
""",
        "outcome": "configured firewall rules using network tags.",
        "interview_qs": """
### 8️⃣ Interview Q&A
**Q1: What is 0.0.0.0/0?**
*Answer:* In CIDR notation, it represents all possible IP addresses. In a firewall rule, it implies "Anywhere" or "The Public Internet".

**Q2: How do generic firewalls differ from GCP firewalls regarding state?**
*Answer:* GCP firewalls are stateful. If I allow a connection TO a server, the server's reply is automatically allowed back. I don't need a separate rule for the reply.
"""
    },
    6: {
        "title": "Subnets & Regions",
        "description": "Organizing your network geographically.",
        "concept": """
### 1️⃣ Plain-English Explanation
We know **Regions** are cities (Iowa, London). **Zones** are specific buildings in that city (Zone A, Zone B).
**Subnets** are the logical containers for your IP addresses in those regions.

### 2️⃣ Real-World Analogy
*   **Region**: The City of New York.
*   **Zone**: The Empire State Building vs The Chrysler Building (Separate power/cooling).
*   **Subnet**: The phone number area code (212 for NYC).

### 3️⃣ Why This Exists (EXAM FOCUS)
*   **High Availability (HA)**: If the Empire State Building loses power (Zone failure), the Chrysler Building is fine.
*   **Disaster Recovery (DR)**: If all of NYC floods (Region failure), you need a backup in London.

### 4️⃣ Key Concepts
1.  **Expandable Subnets**:
    *   You can *expand* a subnet range (e.g., from 256 IPs to 512 IPs) without deleting it.
    *   *Constraint*: You cannot shrink it.
2.  **Private Google Access**:
    *   A checkbox on the subnet.
    *   Allows VMs with **no external IP** to still reach Google APIs (like Cloud Storage or BigQuery). Critical for security!

### 6️⃣ Exam Triggers 🚨
*   **"Expand CIDR"**: You can expand, never shrink.
*   **"Access Storage without Internet"**: Enable **Private Google Access** on the subnet.

### 9️⃣ One-Line Memory Hook 🧠
**Put VMs in different Zones to survive a power outage. Put them in different Regions to survive a hurricane.**
""",
        "hands_on": """
### 5️⃣ Console Walkthrough (STEP-BY-STEP)

**Goal**: Verify Private Google Access.

1.  **Navigate**: **VPC Network** > **Subnets**.
2.  **Click**: The subnet you created (`subnet-usa`).
3.  **Click Edit**.
4.  **Find**: **Private Google Access**.
5.  **Toggle**: On.
6.  **Save**.
    *   *Why?* Now a database server in this subnet (which has no public internet access) can still safely dump its backup files to Cloud Storage. This is a massive security win.
""",
        "outcome": "verified global connectivity over Google's backbone.",
        "interview_qs": """
### 8️⃣ Interview Q&A
**Q1: Can I change the region of a subnet after creating it?**
*Answer:* No. A subnet is strictly bound to a region. You would have to delete it and recreate it.

**Q2: What is the difference between specific Zones (a, b, c)?**
*Answer:* Nothing technically. 'a' is just a label. But physically, they are separate data centers with independent power and cooling to ensure redundancy.
"""
    },
    7: {
        "title": "Week 1 Review & Quiz",
        "description": "Consolidate your knowledge of Core Infra.",
        "concept": """
### 🎓 Week 1 Graduation
You made it through the hardest part: **The Jargon**.
You now speak "Cloud".

### Key Takeaways Checklist
1.  **Compute Engine**: Rented VMs. E2 for normal stuff, C2 for speed, M2 for RAM.
2.  **Disks**: Persistent Disk (Network, Durable) vs Local SSD (Fast, Ephemeral).
3.  **VPC**: Global Network.
4.  **Subnet**: Regional IP range.
5.  **Firewall**: Stateful security. Use Tags!

### Exam Strategy: The Elimination Game
When you see a question:
1.  **Identify the Goal**: "Save Money" vs "High Speed" vs "High Availability".
2.  **Eliminate the Wrong Service**:
    *   If it says "Global Subnet", exclude it (Subnets are Regional).
    *   If it says "Persist data on Local SSD", exclude it (Local SSD is ephemeral).
""",
        "hands_on": """
### 🧠 Mental Gym (Quiz)

**Open the knowledge check below.**
Try to answer these without looking up the cheat sheet.

*   Which machine type is for SAP HANA?
*   Does a VPC cover one region or all regions?
*   How do you stop a Preemptible VM from being deleted? (Hint: You can't!)
""",
        "outcome": "mastered the fundamentals of Google Cloud Infrastructure.",
        "interview_qs": "**Q: Summary Question**\n*Answer:* N/A"
    },

    # WEEK 2: STORAGE & DATABASES
    8: {
        "title": "Cloud Storage (GCS) Buckets",
        "description": "Storing files (images, logs) in the cloud.",
        "concept": """
### Object Storage
Everything here is an **Object** (file) inside a **Bucket** (container). It is **not** a file system (no hierarchal folders, just keys).

**Storage Classes**:
1.  **Standard**: Hot data, frequently accessed (Websites, streaming).
2.  **Nearline**: Once a month (Backups).
3.  **Coldline**: Once a quarter (Disaster recovery).
4.  **Archive**: Once a year (Regulatory logs).
**,
""",
        "hands_on": """
### Lab: Create a Bucket
1.  Go to **Cloud Storage** > **Buckets**.
2.  Click **Create**.
3.  Name: `[unique-id]-my-bucket`.
4.  Location: `Region` (us-central1).
5.  Class: `Standard`.
6.  **Upload** an image file.
7.  ** Permissions**: Click the three dots > Edit Access. Add `allUsers` as `Storage Object Viewer` to make it public.
""",
        "outcome": "created and secured a Cloud Storage bucket.",
        "interview_qs": "**Q: How do you choose between Standard and Coldline storage?**\n*Answer:* Based on access frequency. Frequent access = Standard. Rare access = Coldline/Archive to save money."
    },
    9: {
        "title": "Versioning & Lifecycle Rules",
        "description": "Managing file versions and auto-deletion.",
        "concept": """
### Smart Buckets
*   **Versioning**: Keeps history of overwrites/creates. If you accidentally delete a file, you can restore a past version.
*   **Lifecycle Rules**: Automate cost savings.
    *   *Example:* "Move objects to Coldline if age > 30 days."
    *   *Example:* "Delete objects if age > 365 days."
""",
        "hands_on": """
### Lab: Configure Lifecycle
1.  Open your bucket configuration tab **Lifecycle**.
2.  **Add a rule**:
    *   *Action*: Set to Coldline.
    *   *Condition*: Age is 30 days.
3.  Turn on **Versioning** in the **Protection** tab.
4.  Upload a file `test.txt`. Upload a *new* version of `test.txt`.
5.  Check the "Show deleted/archived" history.
""",
        "outcome": "automated data cost optimization.",
        "interview_qs": "**Q: Can Lifecycle rules affect existing objects?**\n*Answer:* Yes, the rules are evaluated daily against all objects in the bucket."
    },
    10: {
        "title": "Cloud SQL (Relational DB)",
        "description": "Running MySQL/PostgreSQL in the cloud.",
        "concept": """
### Managed Relational Databases
If you need MySQL, PostgreSQL, or SQL Server, use **Cloud SQL**.
*   **Managed**: Google handles backups, patching, and replication.
*   **Vertical Scaling**: Increase CPU/RAM.
*   **Read Replicas**: Copies of DB for faster reading.

**When to use**: Traditional web apps (Wordpress), ERPs, structured data.
""",
        "hands_on": """
### Lab: Spin up MySQL
1.  Go to **SQL**.
2.  Create Instance > **MySQL**.
3.  ID: `my-db`. Password: `root`.
4.  Select `Sandbox` (Development) edition to save money.
5.  **Connect**: Use Cloud Shell.
    `gcloud sql connect my-db --user=root`
6.  Run `SHOW DATABASES;`
""",
        "outcome": "deployed a managed MySQL instance.",
        "interview_qs": "**Q: Difference between Cloud SQL and Spanner?**\n*Answer:* Cloud SQL is regional (harder to scale globally). Cloud Spanner is a globally distributed, horizontally scalable relational database."
    },
    11: {
        "title": "Firestore (NoSQL DB)",
        "description": "Storing app data in documents.",
        "concept": """
### Serverless NoSQL
**Firestore** is a flexible, scalable database for mobile, web, and server development.
*   **Document Model**: Data is stored in documents arranged in collections (JSON-like).
*   **Real-time**: Listeners can update client apps instantly.
*   **Modes**: Native (recommended) vs Datastore mode.

**When to use**: User profiles, game state, product catalogs.
""",
        "hands_on": """
### Lab: Add Data to Firestore
1.  Search **Firestore**.
2.  Select **Native Mode**.
3.  Location: `nam5` (multi-region).
4.  **Start Collection**: `users`.
5.  **Add Document** (Auto-ID):
    *   Field: `username`, Type: string, Value: `cloud_hero`.
    *   Field: `level`, Type: number, Value: `99`.
""",
        "outcome": "stored unstructured data in Firestore.",
        "interview_qs": "**Q: Does Firestore require you to provision servers?**\n*Answer:* No, it is fully serverless and autoscaling."
    },
    12: {
        "title": "Load Balancing Basics",
        "description": "Distributing traffic to multiple VMs.",
        "concept": """
### Traffic Distribution
A **Load Balancer (LB)** sits in front of your VMs and distributes traffic so no single VM is overwhelmed.
*   **HTTP(S) LB**: Layer 7 (Global). Can route based on URL (e.g., `/video` goes to Group A, `/images` goes to Group B).
*   **Network LB**: Layer 4 (Regional). For TCP/UDP traffic.

**Health Checks**: The LB pings your VMs. If one fails, traffic stops going there.
""",
        "hands_on": """
### Lab: Setup an LB (Conceptual)
*Note: Full LB setup takes 15+ mins. We will simulate steps.*
1.  Create an **Instance Group** (IG) of 2 VMs.
2.  Go to **Network Services** > **Load Balancing**.
3.  Create **HTTP(S) Load Balancer**.
4.  **Backend Config**: Point to your Instance Group.
5.  **Frontend Config**: Assign a global IP.
""",
        "outcome": "understood how to scale applications manually.",
        "interview_qs": "**Q: Is the HTTP(S) Load Balancer regional or global?**\n*Answer:* Global. You get a single Anycast IP that works everywhere in the world."
    },
    13: {
        "title": "Content Delivery Network (CDN)",
        "description": "Speeding up your website globally.",
        "concept": """
### Cache at the Edge
**Cloud CDN** caches your content (images, CSS, video) at Google's Edge locations (close to users).
*   **How it works**: Simply check a box on your HTTPS Load Balancer backend.
*   **Benefit**: Faster load times for users, less load on your backend servers.
""",
        "hands_on": """
### Lab: Enabling CDN
1.  Go to your Load Balancer configuration.
2.  Edit the **Backend Service**.
3.  Check the box **Enable Cloud CDN**.
4.  That's it! Google now caches your static responses.
""",
        "outcome": "optimized content delivery latency.",
        "interview_qs": "**Q: What qualifies as 'cacheable' content?**\n*Answer:* Static assets with keys like Cache-Control headers, public read access, and typically HTTP GET requests."
    },
    14: {
        "title": "Week 2 Review & Quiz",
        "description": "Review Storage & Networking.",
        "concept": """
### Week 2 Recap
*   **Storage**: GCS (Objects), SQL (Relational), Firestore (NoSQL).
*   **Networking**: Load Balancing (Global vs Regional), CDN (Caching).
""",
        "hands_on": """
### Review Checklist
1.  Do you know the 4 GCS Storage classes?
2.  Can you explain when to use SQL vs Firestore?
3.  What separates a Global LB from a Regional LB?
""",
        "outcome": "mastered GCP data and traffic services.",
        "interview_qs": "**Q: N/A**"
    },

    # WEEK 3: IAM, OPERATIONS & SECURITY
    15: {
        "title": "IAM (Identity & Access Management)",
        "description": "Who can do what in your project.",
        "concept": """
### The Golden Rule: Least Privilege
**Who** (Identity) can do **What** (Role) on **Which Resource**.

1.  **Members**: Google Account, Service Account, Google Group.
2.  **Roles**:
    *   *Basic* (Owner, Editor, Viewer) -> Avoid using these! Too broad.
    *   *Predefined* (Storage Object Viewer) -> Best practice.
    *   *Custom* -> Granular control.
""",
        "hands_on": """
### Lab: Grant Permissions
1.  Go to **IAM & Admin** > **IAM**.
2.  Click **Grant Access**.
3.  **New Principal**: Enter a friend's email (or your secondary email).
4.  **Assign Role**: `Compute Viewer` (Can see VMs but not change them).
5.  Save.
""",
        "outcome": "secured project access using IAM roles.",
        "interview_qs": "**Q: What is the Principle of Least Privilege?**\n*Answer:* Giving a user only the minimum permissions necessary to do their job, and nothing more."
    },
    16: {
        "title": "Service Accounts",
        "description": "Identities for machines/applications.",
        "concept": """
### ID for Robots
A **Service Account (SA)** is a special Google account that belongs to your application or a VM, not a person.
*   **Key usage**: A VM needs to read from a Bucket. It uses an SA to authenticate.
*   **Keys**: Can be managed by Google (seamless) or User-managed (JSON keys downloaded).
""",
        "hands_on": """
### Lab: Create a Service Account
1.  Go to **IAM & Admin** > **Service Accounts**.
2.  Create Service Account named `app-reader`.
3.  Grant it role `Storage Object Viewer`.
4.  Click **Done**.
5.  (Optional) Attach this SA to a VM instance to let the VM read storage without a password.
""",
        "outcome": "delegated automated permissions securely.",
        "interview_qs": "**Q: Should you check in Service Account JSON keys to GitHub?**\n*Answer:* NEVER. This is a major security risk. Use Workload Identity or managed keys whenever possible."
    },
    17: {
        "title": "Cloud Monitoring (Operations)",
        "description": "Watching CPU usage and logs.",
        "concept": """
### Keeping the Lights On
**Cloud Operations Suite** (formerly Stackdriver) gives you visibility.
*   **Monitoring**: Metrics, Dashboards, Uptime Checks. (e.g., "Is CPU > 80%?").
*   **Alerting**: Send email/SMS if something breaks.
""",
        "hands_on": """
### Lab: Create an Uptime Check
1.  Go to **Monitoring** > **Uptime Checks**.
2.  **Create Uptime Check**.
3.  Target: Your `web-server-1` External IP or LB IP.
4.  Protocol: HTTP.
5.  Test.
6.  Save. Google will now ping your site from around the world every 1-5 mins.
""",
        "outcome": "setup observability for infrastructure.",
        "interview_qs": "**Q: What is the difference between Monitoring and Logging?**\n*Answer:* Monitoring tracks *metrics* (numbers, trends). Logging tracks *events* (text records of what happened)."
    },
    18: {
        "title": "Cloud Logging",
        "description": "Reading system logs to debug errors.",
        "concept": """
### The Source of Truth
Every action in GCP produces a log.
*   **Audit Logs**: "Who did what?" (Admin activity).
*   **App Logs**: Output from your code (`print("error")`).
*   **Log Router**: You can export logs to BigQuery (for analysis) or Storage (for compliance).
""",
        "hands_on": """
### Lab: Search Logs
1.  Go to **Logging** > **Logs Explorer**.
2.  In the Query builder, select Resource Type: `VM Instance`.
3.  Click **Run Query**.
4.  See the entries. Try filtering by Severity `ERROR` (hopefully none!).
""",
        "outcome": "debugged issues using the Logs Explorer.",
        "interview_qs": "**Q: Where are Admin Activity logs stored?**\n*Answer:* They are stored in the `_Required` bucket and retained for 400 days by default (immutable)."
    },
    19: {
        "title": "Billing & Budgets",
        "description": "Setting alerts so you don't overspend.",
        "concept": """
### Don't Go Broke
*   **Billing Account**: Pays for the projects. Can be linked to multiple projects.
*   **Budgets**: Set a limit (e.g., $100).
*   **Alerts**: Get an email when you hit 50%, 90%, 100% of budget. *Note: Alerts do NOT stop services automatically, they just warn you.*
""",
        "hands_on": """
### Lab: Set a Budget
1.  Go to **Billing** > **Budgets & alerts**.
2.  Create Budget.
3.  Amount: $10.00.
4.  Thresholds: 50%, 90%, 100%.
5.  **Finish**. This is the most important step for any student!
""",
        "outcome": "protected against surprise cloud bills.",
        "interview_qs": "**Q: Does a budget alert stop your VM instances to save money?**\n*Answer:* No. It only notifies you. You must setup a programmatic action (Cloud Functions) to stop resources."
    },
    20: {
        "title": "Security Groups vs Firewalls",
        "description": "Deep dive into securing instances.",
        "concept": """
### Multiple Layers of Defense
*   **Firewall**: Acts at the subnet/VM level.
*   **IAP (Identity Aware Proxy)**: Lets you SSH into VMs **without** a public IP. This is cleaner and safer than opening port 22 to the world.
""",
        "hands_on": """
### Lab: SSH via IAP (Tunnel)
1.  Go to **Security** > **Identity-Aware Proxy**.
2.  Enable the API.
3.  Go to your VM. Remove its external IP and block port 22 firewall.
4.  Try to SSH from Console (using IAP tunneling).
5.  *Result:* Secure access without public internet exposure.
""",
        "outcome": "implemented advanced access security.",
        "interview_qs": "**Q: Why use IAP for SSH?**\n*Answer:* It removes the need for public IP addresses on VMs, reducing the attack surface significantly."
    },
    21: {
        "title": "Week 3 Review & Quiz",
        "description": "IAM, Operations, and Security review.",
        "concept": """
### Week 3 Recap
You are now a safe and responsible cloud engineer.
*   **IAM**: Least Privilege, Principals, Roles.
*   **Ops**: Monitoring metrics and reading Logs.
*   **Cost**: Budgets never sleep.
""",
        "hands_on": """
### Knowledge Check
1.  Who manages Service Account keys?
2.  What is the difference between Primitive and Predefined roles?
3.  How do you stop a bill from going over $100?
""",
        "outcome": "mastered governance and operations.",
        "interview_qs": "**Q: N/A**"
    },

    # WEEK 4: ADVANCED SERVICES & CERTIFICATION
    22: {
        "title": "Google Kubernetes Engine (GKE)",
        "description": "Introduction to Containers and Pods.",
        "concept": """
### The Vessel of Modern Apps
*   **Docker/Container**: Packages code + dependencies. Runs anywhere.
*   **Kubernetes (K8s)**: Orchestrates containers. Manages scaling, healing, and updates.
*   **GKE**: Google's managed K8s. They manage the master node; you manage the workers (nodes).
""",
        "hands_on": """
### Lab: Deploy Nginx on GKE
1.  Go to **Kubernetes Engine** > **Clusters**.
2.  Create **Autopilot** cluster (easiest).
3.  Click **Connect** > Run in Cloud Shell.
4.  Run: `kubectl create deployment web --image=nginx`
5.  Run: `kubectl expose deployment web --port=80 --type=LoadBalancer`
6.  Wait for External IP. Visit it!
""",
        "outcome": "deployed a containerized app on GKE.",
        "interview_qs": "**Q: Difference between GKE Standard and Autopilot?**\n*Answer:* Standard gives you control over nodes. Autopilot manages the nodes/infrastructure completely for you, charging per pod."
    },
    23: {
        "title": "App Engine (PaaS)",
        "description": "Deploying code without managing servers.",
        "concept": """
### Just Code
**App Engine** was Google's first product.
*   **Standard Environment**: Restricted languages (Python, Java, Go), instant scaling to zero, restricted filesystem.
*   **Flexible Environment**: Any Docker container, access to background processes, slower startup.
""",
        "hands_on": """
### Lab: Deploy Hello World
1.  Open Cloud Shell editor.
2.  Create `app.yaml` (`runtime: python39`).
3.  Create `main.py` (Simple Flask app).
4.  Run `gcloud app deploy`.
5.  Visit `[project-id].appspot.com`.
""",
        "outcome": "deployed a serverless Platform-as-a-Service app.",
        "interview_qs": "**Q: Can App Engine Standard scale to zero?**\n*Answer:* Yes, if no traffic is coming in, it scales to 0 instances (costing $0). Flexible env requires at least 1 instance."
    },
    24: {
        "title": "Cloud Functions (Serverless)",
        "description": "Running code in response to events.",
        "concept": """
### Event Driven Glue
**Cloud Functions** are small snippets of code that run when something happens.
*   **Triggers**: HTTP request, File uploaded to Storage, Pub/Sub message.
*   **Use case**: "When an image is uploaded, resize it."
""",
        "hands_on": """
### Lab: The Hello World Function
1.  Search **Cloud Functions**. 
2.  Create Function.
3.  Trigger: **HTTP**.
4.  Runtime: Python 3.9. Use default Code.
5.  Deploy.
6.  Click the Testing tab > **Test the function**.
""",
        "outcome": "deployed an event-driven function.",
        "interview_qs": "**Q: Maximum execution time for a Cloud Function?**\n*Answer:* Typically 9 minutes (Gen 1) or 60 minutes (Gen 2) for HTTP."
    },
    25: {
        "title": "Cloud Run",
        "description": "Serverless for containers.",
        "concept": """
### The Best of Both Worlds
**Cloud Run** lets you run any **Container** (like GKE) but completely **Serverless** (like App Engine).
*   **Stateless**: Requests can go to any instance.
*   **Concurrency**: One instance can handle multiple requests (unlike Functions which is 1 at a time).
*   **Traffic Splitting**: Easy Canary deployments (send 10% traffic to V2).
""",
        "hands_on": """
### Lab: Deploy Container to Cloud Run
1.  Search **Cloud Run**.
2.  Create Service.
3.  Select Demo Container (`us-docker.pkg.dev/cloudrun/container/hello`).
4.  Allow unauthenticated invocations (Public).
5.  Create.
6.  You have a live HTTPS URL in 30 seconds.
""",
        "outcome": "deployed a serverless container with Cloud Run.",
        "interview_qs": "**Q: How to charge for Cloud Run?**\n*Answer:* You pay for CPU/Memory only while the request is being processed (rounded to 100ms)."
    },
    26: {
        "title": "Infrastructure as Code (Terraform)",
        "description": "Automating resource creation.",
        "concept": """
### Code your Infrastructure
Instead of clicking buttons, define your infra in text files (`.tf`).
*   **Declarative**: You say "I want 3 VMs" (State desire), Terraform makes it happen.
*   **Reproducible**: Delete everything and recreate it exactly in minutes.
""",
        "hands_on": """
### Lab: Terraform Basics
1.  Open Cloud Shell.
2.  Create `main.tf`:
    ```hcl
    resource "google_compute_instance" "vm" {
      name         = "terraform-vm"
      machine_type = "e2-micro"
      zone         = "us-central1-a"
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-11"
        }
      }
      network_interface {
        network = "default"
      }
    }
    ```
3.  Run `terraform init`.
4.  Run `terraform apply`.
""",
        "outcome": "provisioned infrastructure using Terraform code.",
        "interview_qs": "**Q: What is the terraform state file?**\n*Answer:* A file that tracks the mapping between your resource definitions and real world resources."
    },
    27: {
        "title": "Sample Exam Questions (Set 1)",
        "description": "Practice specifically for the ACE exam.",
        "concept": """
### Exam Practice: IAM & Compute
1.  **Scenario**: You need to grant a contractor access to view GCS buckets but not read the files inside.
    *   *Role*: `Storage Object Viewer` vs `Storage Legacy Bucket Reader`.
2.  **Scenario**: A VM needs to restart automatically if it crashes.
    *   *Feature*: Managed Instance Group (MIG) autohealing.
""",
        "hands_on": """
### Activity
Review the official Google Cloud ACE Exam Guide.
""",
        "outcome": "practiced core exam scenarios.",
        "interview_qs": "N/A"
    },
    28: {
        "title": "Sample Exam Questions (Set 2)",
        "description": "More practice questions.",
        "concept": """
### Exam Practice: Networking & Storage
1.  **Scenario**: You need a global database with SQL semantics.
    *   *Service*: Cloud Spanner.
2.  **Scenario**: Secure connection between on-premise and Cloud without public internet.
    *   *Service*: Cloud Interconnect (Dedicated or Partner) or Cloud VPN.
""",
        "hands_on": """
### Activity
Take a 20-question practice test online (e.g., Google's sample questions).
""",
        "outcome": "refined exam readiness.",
        "interview_qs": "N/A"
    },
    29: {
        "title": "Deployment Manager & Marketplace",
        "description": "Google's native IaC tool.",
        "concept": """
### Native IaC
While Terraform is industry standard, **Deployment Manager** is GCP's native tool using YAML/Python.
*   **Marketplace**: Launch click-to-deploy solutions (e.g., Wordpress by Bitnami) which use Deployment Manager under the hood.
""",
        "hands_on": """
### Lab: Marketplace Launch
1.  Search **Marketplace**.
2.  Search **Nginx**.
3.  Click **Launch**.
4.  See how it orchestrates VMs, Firewalls, and Disks for you automatically.
""",
        "outcome": "deployed complex solutions via Marketplace.",
        "interview_qs": "**Q: Terraform vs Deployment Manager?**\n*Answer:* Terraform is multi-cloud. Deployment Manager is GCP native."
    },
    30: {
        "title": "Final Readiness & Certification Tips",
        "description": "How to register and take the exam.",
        "concept": """
### You Made It! 🎓
You have completed the 30-day roadmap.

**Exam Day Tips**:
1.  **Read carefully**: Look for keywords like "Cost-effective" (Spot VMs, Coldline) vs "High Availability" (Multi-zone, Multi-region).
2.  **Eliminate**: Usually 2 options are obviously wrong.
3.  **Time**: You have 2 hours for 50 questions.

**Registration**: Go to Webassessor and book your slot. Good luck!
""",
        "hands_on": """
### Final Task
1.  Review your notes.
2.  Clean up your project! Delete the project to avoid billing.
    `gcloud projects delete [YOUR_PROJECT_ID]`
""",
        "outcome": "completed the 30-day GCP pathway.",
        "interview_qs": "**Q: What's next?**\n*Answer:* Professional Cloud Architect."
    }
}
