from django.core.management.base import BaseCommand
from curriculum.models import Week, Day

class Command(BaseCommand):
    help = 'Populates the database with Week 1 GCP content'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating Week 1 content...')

        # Ensure Week 1 exists
        week1, created = Week.objects.get_or_create(
            number=1,
            defaults={'description': 'GCP Foundations, Infrastructure, Billing, and Core Services (Compute & Storage)'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Week 1'))

        days_data = [
            {
                "number": 1,
                "title": "What is Cloud Computing?",
                "outcome": "Understand CapEx vs OpEx and the 'Rental' model of Cloud.",
                "description": "Foundation concepts: Cloud definition, Analogies, and Why it exists.",
                "concept_content": """# SECTION 1: What is Cloud Computing? (The Foundation)

## 1️⃣ Plain-English Explanation
Imagine you want to live in a house. You have two choices:
1.  **Build your own house:** You buy the land, bricks, plumbing, and electricity. You are responsible for repairs, security, and upgrades. If you need more space, you have to build a new room yourself.
2.  **Rent a hotel room:** You just check in. The hotel handles the maintenance, security, and electricity. If you need a bigger suite, you just upgrade your booking. When you leave, you stop paying.

**Cloud Computing is the "Hotel" approach for computers.** instead of buying and maintaining physical servers (computers) in your own office, you "rent" access to Google's massive data centers over the internet. You pay only for what you use, and Google handles the hard stuff (power, cooling, hardware repairs).

## 2️⃣ Real-World Analogy
**The "Utility" Analogy (Electricity)**

*   **On-Premises (Old Way):** Buying a generator for your house. You pay for the generator upfront, buy fuel, fix it when it breaks, and if you need more power than it can provide, the lights go out.
*   **Cloud Computing (New Way):** Plugging into the wall grid. The power company generates the electricity. You just flip the switch and pay a monthly bill based on how much you used.

## 3️⃣ Why This Exists (Exam Focus)
For the exam and interviews, remember **Cost** and **Speed**.
*   **CapEx to OpEx:** Companies switch from **Capital Expenditure** (buying hardware upfront) to **Operational Expenditure** (paying monthly for what they use). This frees up cash.
*   **Agility:** Instead of waiting weeks to order and install a new server, a developer can click a button and get one in seconds.

## 4️⃣ How It Works (Simple Mental Model)
Think of Google Cloud as a massive vending machine for IT resources.
1.  **The Provider (Google):** Owns physical data centers full of servers, hard drives, and networking gear.
2.  **The Internet:** The wire connecting you to the data centers.
3.  **The User (You):** You use a web browser (Console) or command line (CLI) to request resources. "I need a computer with 4 CPUs."
4.  **Virtualization:** Google's software slices up its massive physical machines into smaller "Virtual Machines" (VMs) for you to use.

## 6️⃣ Key Exam Triggers 🚨
If you see these keywords in an exam question, think "Cloud Benefits":
*   **"Variable Expense"**: Paying only for what you use (OpEx).
*   **"Economies of Scale"**: Lower prices because Google buys hardware in bulk.
*   **"Elasticity"**: Automatically scaling up (adding computers) when users spike, and scaling down (removing them) when they leave (e.g., Black Friday sales).
*   **"Go Global in Minutes"**: Deploying your app to users in Asia, Europe, and US with a few clicks.

## 7️⃣ Compare With Related Concepts

| Feature | On-Premises (Private Data Center) | Cloud Computing (GCP) |
| :--- | :--- | :--- |
| **Cost Model** | CapEx (Buy hardware upfront) | OpEx (Pay-as-you-go) |
| **Maintenance** | You fix broken hard drives | Google fixes them invisible to you |
| **Scalability** | Hard (Buy more servers, wait weeks) | Easy (Click a button, instant) |
| **Security** | You control everything (Physical + Digital) | Shared Responsibility (Google protects hardware, you protect files) |

### The "As-a-Service" Pyramid
*   **IaaS (Infrastructure as a Service):** You rent the raw hardware (VMs). *Example: Compute Engine.*
*   **PaaS (Platform as a Service):** You upload code, Google runs it. No server management. *Example: App Engine, Cloud Functions.*
*   **SaaS (Software as a Service):** You just use the software. *Example: Gmail, Google Drive.*

## 9️⃣ One-Line Memory Hook 🧠
> "Cloud Computing is just **someone else's computer** that you pay for like **electricity**."
""",
                "hands_on_content": """## 5️⃣ GCP Console Walkthrough (Step-by-step)
*   **Step 1:** Go to `console.cloud.google.com`.
*   **Step 2:** Log in with your Google account.
*   **Step 3:** You land on the **Dashboard**. Look at the top blue bar—this is your **Project Selector**. Everything in GCP lives inside a "Project".
*   **Step 4:** Open the **Navigation Menu** (the "Hamburger" icon 🍔 in the top left).
*   **Step 5:** Scroll to **Compute Engine** > **VM Instances**.
*   **Step 6:** This is where you would "rent" a computer. If you clicked "Create Instance", you'd be spinning up a cloud server!
""",
                "interview_questions": """## 8️⃣ Interview-Ready Q&A
**Q: "Can you explain the difference between Scalability and Elasticity?"**
*   **A:** **Scalability** is the *ability* to handle growth (like a gym having room for more members). **Elasticity** is the *automatic* action of stretching and shrinking based on demand (like a rubber band expanding when pulled and snapping back instantly). Cloud methods are elastic.

**Q: "Why would a bank choose Hybrid Cloud instead of going 100% public?"**
*   **A:** Compliance and Regulation. They might keep sensitive customer database on-premises (for total control) but run their public-facing website on the Cloud (to handle high traffic). This mix is **Hybrid Cloud**.
"""
            },
            {
                "number": 2,
                "title": "GCP Structure (Organization, Projects, Regions)",
                "outcome": "Master the Resource Hierarchy and Global Infrastructure logic.",
                "description": "Hierarchy (Org > Folder > Project) and Geography (Regions vs Zones).",
                "concept_content": """# SECTION 2: GCP Structure (Organization, Folders, Projects, Regions, Zones)

## 1️⃣ Plain-English Explanation
Everything in Google Cloud needs to live somewhere. Just like files on your computer live in folders, and folders live on a hard drive, GCP has a specific hierarchy.

*   **The Resource Hierarchy:** This is how you organize your permission and billing. It shuts down chaos.
*   **The Global Infrastructure:** This is the physical location of the computers you are renting.

You can't just "create a server" floating in space. You must first create a **Project** (a billing bucket), and then tell Google **where** (Region/Zone) you want that server to physically sit.

## 2️⃣ Real-World Analogy
**The "Corporate Head Office" Analogy**

1.  **Organization (The Company CEO):** The top level. Policies set here (e.g., "No external emails") apply to everyone below.
2.  **Folders (Departments):** Marketing, HR, IT. Used to group teams.
3.  **Projects (Specific Jobs):** "Summer Ad Campaign" or "New Payroll System". This is where the work actually happens.
4.  **Resources (The Desks):** The actual VMs, Databases, and Storage buckets used to do the job.

**The "Real Estate" Analogy (Regions vs Zones)**
*   **Region:** A City (e.g., London).
*   **Zone:** A specific building in that city (e.g., Building A, Building B, Building C).
*   *Why?* If Building A loses power, Building B is still safe. If the whole City floods (Region failure), both are down.

## 3️⃣ Why This Exists (Exam Focus)
1.  **Billing Isolation:** "Projects" are the distinct billing unit. You can send the invoice for the "Marketing Project" to the Marketing team and "IT Project" to IT.
2.  **Policy Inheritance:** If you enforce a security rule at the **Organization** node, it automatically trickles down to every Folder and Project. You don't have to secure 1,000 servers individually.

## 4️⃣ How It Works (Simple Mental Model)
*   **Hierarchy:** Organization ➔ Folders (Optional) ➔ Projects ➔ Resources.
*   **Geography:** Global (Multi-Region) ➔ Region ➔ Zone.

**Important:** **Resources** (like VMs) are *Zonal*. **Static IP addresses** are *Regional*. **Images** are *Global*. You must know the "scope" of a resource for the exam.

## 6️⃣ Key Exam Triggers 🚨
*   **"Low Latency"**: Choose a Region *closest* to your users.
*   **"High Availability (HA)"**: Distribute servers across multiple **Zones** (in case one building fails).
*   **"Disaster Recovery (DR)"**: Distribute servers across multiple **Regions** (in case an earthquake hits the city).
*   **"Data Compliance / GDPR"**: You MUST store data in a specific Region (e.g., `europe-west3` in Germany) to keep it legal.

## 7️⃣ Region vs Zone Clarity
This is the #1 confusion spot.

*   **Region:** A geographical area (usually involves 3-4 separate zones).
    *   *Example:* `us-central1` (Iowa), `asia-south1` (Mumbai).
*   **Zone:** An isolated location *within* a region. Zones have independent power, cooling, and networking.
    *   *Example:* `us-central1-a`, `us-central1-b`.
    *   *Latency:* Networking between zones in the same region is super fast (microseconds).

**Cost vs Latency vs Compliance:**
*   **Cost:** Some regions are cheaper (e.g., US) than others (e.g., Brazil/Australia).
*   **Latency:** Closer to user = Faster.
*   **Compliance:** Laws might force you to stay in one country. *Compliance overrides Cost and Latency.*

## 9️⃣ One-Line Memory Hook 🧠
> "**Projects** pay the bills; **Zones** stop the failures."
""",
                "hands_on_content": """## 5️⃣ GCP Console Walkthrough (Step-by-step)
**Seeing the Hierarchy:**
*   **Step 1:** Log in to `console.cloud.google.com`.
*   **Step 2:** Look at the top bar next to the Google Cloud logo. You will see a dropdown with a project name (e.g., "My First Project").
*   **Step 3:** Click it to open the **Resource Manager**.
*   **Step 4:** If you have an Organization (like a corporate account), you will see your domain (e.g., `company.com`) at the top. Below it, folders, and then projects.

**Seeing Regions & Zones:**
*   **Step 1:** Go to the Navigation Menu 🍔 > **Compute Engine** > **VM Instances**.
*   **Step 2:** Click **Create Instance**.
*   **Step 3:** Look at the **Region** dropdown (e.g., `us-central1 (Iowa)`).
*   **Step 4:** Look at the **Zone** dropdown (e.g., `us-central1-a`, `us-central1-b`).
*   **Step 5:** Note that you *must* pick a Zone. A VM cannot exist in two buildings at once!
""",
                "interview_questions": """## 8️⃣ Interview-Ready Q&A
**Q: "I deleted a Project. Can I get it back?"**
*   **A:** Yes, but only for **30 days**. It enters a "soft delete" state. After 30 days, it is completely purged and unrecoverable.

**Q: "What is the difference between a Label and a Tag?"**
*   **A:** Oh, this is a distinct one!
    *   **Labels** are for *organization/billing* (e.g., `dept: marketing`). You can query billing reports by label.
    *   **Tags** are for *networking/security* (e.g., `allow-http`). You use tags to apply firewall rules.
"""
            },
            {
                "number": 3,
                "title": "Billing, Free Tier, Quotas",
                "outcome": "Understand how to control costs, set budgets, and avoid quotas.",
                "description": "Billing Accounts, Budgets, Alerts, and Hard/Soft Limits.",
                "concept_content": """# SECTION 3: GCP Billing, Free Tier, Quotas & Cost Control

## 1️⃣ Plain-English Explanation
In the last section, we learned that a **Project** is like a "Bucket" for your resources. But who pays for that bucket?

*   **The Billing Account:** This is the credit card or bank account. You attach Projects to a Billing Account. If you don't attach one, the Project can't run anything (except Free Tier stuff).
*   **Budgets & Alerts:** These are your safety guards. You tell Google, "If I spend more than $50, scream at me via email."
*   **Quotas:** These are "hard limits" to prevent you from accidentally launching 10,000 servers and going bankrupt in an hour.

## 2️⃣ Real-World Analogy
**The "Teenager with a Credit Card" Analogy**

1.  **Billing Account:** The parent's Credit Card.
2.  **Project:** The Teenager's shopping cart. The parent links the card to the cart so the transaction goes through.
3.  **Budgets & Alerts:** The parent saying, "Text me if you spend more than $50." (Note: The store *still* lets you spend more, it just warns the parent).
4.  **Quotas:** The Credit Card Limit (e.g., $500 max). The machine will literally decline the transaction if you try to go over.

## 3️⃣ Why This Exists (Exam Focus)
*   **Control:** Large companies have many departments. They can have **One** Billing Account (paid by Finance) linked to **Many** Projects (Marketing, IT, HR).
*   **Safety:** The cloud scales infinitely. Without Quotas and Budgets, a coding error (infinite loop creating VMs) could cost millions of dollars overnight.

## 4️⃣ How It Works (Simple Mental Model)
*   **Hierarchy:** Billing Checking Account ➔ Linked to Project ➔ Pays for Resources (VMs, Storage).
*   **One-to-Many:** One Billing Account can pay for MANY Projects.
*   **Many-to-One:** A Project can only have ONE Billing Account at a time.

## 6️⃣ Key Exam Triggers 🚨
*   **"Hard Limit" vs "Warning"**:
    *   **Quotas** are HARD limits. (The action fails).
    *   **Budgets** are WARNINGS. (The spending continues, you just get an email).
*   **"CapEx vs OpEx"**: Cloud is OpEx (Operational Expenditure). You pay for what you use.
*   **"Disable Billing"**: To stop spending *immediately*, you must disable billing on the Project. This stops all services.

## 7️⃣ Free Tier vs Free Trial vs Quotas

| Feature | What is it? | Exam Note |
| :--- | :--- | :--- |
| **Free Trial** | $300 credit for 90 days. | Once it's gone, it's gone. |
| **Free Tier** | "Always Free" limits (e.g., 1 tiny VM per month forever). | Available to everyone, even after trial ends. |
| **Quotas** | Limits on *how many* resources you can create (e.g., Max 5 VMs). | Protects Google (from running out of hardware) and You (from accidental spend). |

**Beginner Mistake:** Thinking a "Budget Alert" will automatically shut down your VMs. **IT WILL NOT.** It only sends an email. To shut things down automatically, you need to write a special script (Cloud Function) triggered by the alert, which is an advanced topic.

## 9️⃣ One-Line Memory Hook 🧠
> "**Budgets** bark (alert); **Quotas** bite (blocks)."
""",
                "hands_on_content": """## 5️⃣ GCP Console Walkthrough (Step-by-step)
**Checking Billing:**
*   **Step 1:** Go to `console.cloud.google.com`.
*   **Step 2:** Open the Navigation Menu 🍔 and scroll down to **Billing**.
*   **Step 3:** If you are the admin, you see the "Overview" with current costs.

**Creating a Budget Alert (CRITICAL STEP):**
*   **Step 1:** In the Billing section, click **Budgets & alerts** on the left.
*   **Step 2:** Click **Create Budget**.
*   **Step 3:** Name it "Stop-Me-From-Bankruptcy".
*   **Step 4:** Set amount: **$10** (or whatever you like).
*   **Step 5:** Set Thresholds: Trigger at 50%, 90%, and 100%.
*   **Step 6:** Check "Email alerts to billing admins". **Done.**
""",
                "interview_questions": """## 8️⃣ Interview-Ready Q&A
**Q: "We need to ensure a specific project never spends more than $1,000. Can we set a hard cap?"**
*   **A:** Native GCP Budgets send alerts, they don't stop spending. To enforce a hard cap, we would need to set up a programmatic action (using Pub/Sub and Cloud Functions) to disable billing when the cap is reached.

**Q: "I'm trying to create a GPU instance but I get a 'Quota Exceeded' error. I have money in the account. What's wrong?"**
*   **A:** You hit a resource quota. New accounts often have 0 GPU quota by default to prevent fraud. You must request a **Quota Increase** from support.
"""
            },
            {
                "number": 4,
                "title": "Compute Engine (VMs)",
                "outcome": "Learn to manage Virtual Machines, understand Machine Families, and Zonal nature.",
                "description": "VM Basics, Machine Types (General vs Compute vs Memory), and Zones.",
                "concept_content": """# SECTION 4: Compute Engine (Virtual Machines)

## 1️⃣ Plain-English Explanation
Imagine you are a gamer. You want to play the latest high-end game, but you only have a cheap laptop.
You could go to a "Cyber Cafe" (remember those?) and rent a super-powerful PC for $2 an hour.

*   You don't own the PC.
*   You use it for 3 hours.
*   You install your game, play it, and then log off.
*   You pay $6.

**Compute Engine** is Google's Cyber Cafe. You rent a "Virtual Machine" (VM). It looks and feels exactly like a real computer (Windows or Linux), but it exists in Google's data center. You can install whatever software you want on it.

## 2️⃣ Why VMs still matter
In a world of serverless (where you just write code), why do we still rent raw computers?
*   **Legacy Apps:** Old software written 10 years ago needs a full Operating System (OS). It can't run on modern serverless platforms.
*   **Total Control:** Sometimes you need to tweak the Kernel or install specific drivers. Only a VM gives you this level of access.

## 3️⃣ Machine Types & Families (Simple)
When you rent a car, you choose based on your need: "Truck" for hauling, "Ferrari" for speed, "Sedan" for cheap travel.
GCP has **Machine Families**:

*   **E2 / N1 (General Purpose):** The "Honda Civic". Balanced price and performance. Good for web servers.
*   **C2 (Compute Optimized):** The "Ferrari". Super fast processor. Good for video rendering or gaming.
*   **M2 (Memory Optimized):** The "Dump Truck". Massive amounts of RAM (up to 12TB!). Good for giant databases.

## 4️⃣ Zones & Disks Relationship
**CRITICAL EXAM CONCEPT:**
A VM is a **Zonal Resource**. It lives in ONE specific Zone (e.g., `us-central1-a`).
The Hard Drive (Persistent Disk) attached to it is *also* **Zonal**.
**You CANNOT attach a Disk in Zone A to a VM in Zone B.** They must be in the same building!

## 6️⃣ Exam Traps (Zonal vs Regional) 🚨
*   **Trap:** "Your VM went down because the Zone failed. How do you ensure it survives next time?"
    *   *Wrong Answer:* "Take a snapshot." (Too slow).
    *   *Right Answer:* "Use a **Managed Instance Group (MIG)** to automatically run VMs in *multiple* zones."
*   **Trap:** "You need to move a VM from Zone A to Zone B."
    *   *Solution:* You cannot "move" it. You must **Snapshot** the disk ➔ Create a **New Disk** in Zone B from that snapshot ➔ Create a **New VM** in Zone B.

## 7️⃣ Comparison: VM vs App Engine vs Cloud Run

| Feature | Compute Engine (VM) | App Engine | Cloud Run |
| :--- | :--- | :--- | :--- |
| **Analogy** | Renting a Car | Taking a Taxi | Renting a Scooter |
| **Control** | High (OS access) | Low (Just code) | Medium (Container) |
| **Ops Effort** | High (Patch OS, Security) | Low (Google handles OS) | Low (Google handles OS) |
| **Use Case** | Legacy apps, Databases | Web Apps, Standard code | Microservices, Containers |

## 9️⃣ One-Line Memory Hook 🧠
> "Compute Engine is just a **remote control** for a computer in Google's datacenter."
""",
                "hands_on_content": """## 5️⃣ Step-by-Step VM Creation
1.  **Menu:** Compute Engine > VM Instances.
2.  **Name:** Must be lowercase (e.g., `my-web-server`).
3.  **Region/Zone:** Pick where it lives (e.g., `us-central1-a`).
4.  **Machine Type:** Pick your "Car" (e.g., `e2-medium` - 2 vCPU, 4GB RAM).
5.  **Boot Disk:** Pick your OS (Debian, Ubuntu, Windows Server).
6.  **Firewall:** Check "Allow HTTP traffic" if it's a website.
7.  **Create:** Wait 30 seconds.
8.  **Connect:** Click the "SSH" button to open a terminal instantly in your browser.
""",
                "interview_questions": """## 8️⃣ Interview-Ready Q&A
**Q: "I cannot SSH into my new VM. What is the most likely reason?"**
*   **A:** 99% of the time, it's a **Firewall Rule**. You forgot to allow "TCP port 22" (SSH) from your IP address to the VM.

**Q: "What is a Preemptible (or Spot) VM?"**
*   **A:** It's a "Discount VM" (up to 91% cheaper!) that Google can shut down at any second if they need the capacity back. Great for batch jobs (converting videos), terrible for hosting a website.
"""
            },
            {
                "number": 5,
                "title": "Disks & Storage Basics",
                "outcome": "Distinguish between Persistent Disks and Local SSDs.",
                "description": "Persistent Disk (PD) types, Local SSDs, boot disks, and attaching storage.",
                "concept_content": """# SECTION 5: Disks & Storage Basics

## 1️⃣ Plain-English Explanation
When you buy a laptop, it comes with a hard drive. If the laptop breaks, the hard drive usually still has your files.
In the cloud, we separate the **Computer** (VM) from the **Hard Drive** (Persistent Disk).

*   **Persistent Disk (PD):** A network hard drive. It lives in the same building (Zone) as your VM. If you delete the VM, the disk *can* stay alive (if you configured it to).
*   **Local SSD:** A super-fast hard drive physically plugged into the server motherboard. It is fleeting. If the VM turns off, the data on the Local SSD is gone **forever**.

## 2️⃣ Persistent Disk vs Local SSD (The Analogy)
*   **Persistent Disk:** Your **External USB Drive**. You can unplug it from one computer and plug it into another. It’s reliable.
*   **Local SSD:** The **RAM** (almost). It’s incredibly fast, but if you reboot or shut down, it gets wiped clean (Ephemeral). *Use it for "Swap" or temp cache only.*

## 3️⃣ Boot Disk vs Data Disk
*   **Boot Disk:** Contains the Operating System (Windows C: Drive). Every VM requires one.
*   **Data Disk:** Additional space (D: Drive). You can attach many of these.

## 4️⃣ Attach/Detach Disks (Exam Focus)
*   **Attach:** You can attach a disk to a running VM (Hot Attach).
*   **Resize:** You can increase the size of a disk while the VM is running (Upsizing is easy).
    *   *Trap:* You CANNOT decrease the size. You can only make it bigger.
*   **Detach:** You must unmount it from the OS first, then click detach.

## 5️⃣ Common Disk Types (Speed vs Cost)
1.  **Standard Persistent Disk (HDD):** Cheap, slow, magnetic. good for backups.
2.  **Balanced Persistent Disk (SSD):** Middle ground. Best for most web apps.
3.  **SSD Persistent Disk:** Fast. Good for databases.
4.  **Extreme Persistent Disk:** Insanely fast. For heavy enterprise databases (SAP HANA).

## 7️⃣ Comparison Table

| Feature | Persistent Disk (PD) | Local SSD |
| :--- | :--- | :--- |
| **Speed** | Fast (Network attached) | Extreme (Physically attached) |
| **Durability** | High (Data survives reboots) | None (Data dies on stop) |
| **Migration** | Can move to another VM | Locked to one VM |
| **Max Size** | 64 TB | 9 TB (distributed in 375GB chunks) |

## 9️⃣ One-Line Memory Hook 🧠
> "Persistent Disks are **USB sticks** (moveable); Local SSDs are **RAM** (fast but forgetful)."
""",
                "hands_on_content": """## 6️⃣ Console Walkthrough
1.  **Go to:** Compute Engine > Disks.
2.  **Create:** Click "Create Disk".
3.  **Region/Zone:** MUST match your VM.
4.  **Source:** "Blank disk" (empty) or "Image" (with OS).
5.  **Attach:** Go to VM > Edit > Additional Disks > Attach Existing Disk.
""",
                "interview_questions": """## 8️⃣ Interview-Ready Q&A
**Q: "I deleted my VM and my important database data is gone! Why?"**
*   **A:** When creating a VM, there is a checkbox: *"Delete boot disk when instance is deleted"*. It is checked by default. You should have unchecked it or used a separate **Data Disk**.

**Q: "Can I share one disk between two VMs?"**
*   **A:** Yes, but only in **Read-Only** mode (Multi-writer is possible but very complex and rare, usually for specific clusters like Oracle RAC).
"""
            },
            {
                "number": 6,
                "title": "Cloud Storage (Buckets)",
                "outcome": "Understand Object Storage, Storage Classes, and life-cycle policies.",
                "description": "Buckets, Objects, Standard vs Archive classes.",
                "concept_content": """# SECTION 6: Cloud Storage (Buckets)

## 1️⃣ Plain-English Explanation
Think of your computer. You have folders on your desktop where you keep files.
Now think of Google Drive. You upload a file, and you can share a link so your friend in Japan can download it.

**Cloud Storage** is essentially a programmable "Google Drive" for your applications.
*   It is **Serverless**: You don't need a VM.
*   It is **Infinite**: You can store 1 file or 1 billion files.
*   It is **Global**: Accessible from anywhere in the world (via HTTP).

We store "Objects" (files) inside "Buckets" (containers).

## 2️⃣ Buckets & Objects
*   **Bucket:** The container. Must have a **globally unique name** (like a URL).
    *   *Example:* `my-awesome-cat-photos`. If I take this name, you cannot have it.
*   **Object:** The file inside. (e.g., `cat.jpg`). Objects are **Immutable** (you cannot edit line 10 of a file; you must overwrite the whole file).

## 3️⃣ Storage Classes (The "Temperature" Analogy)
How frequently do you need to touch your data?

1.  **Standard (Hot):**
    *   *Use case:* Websites, streaming videos, mobile apps.
    *   *Cost:* High storage cost, LOW access cost.
2.  **Nearline (Warm):**
    *   *Use case:* Backups you might need once a month.
    *   *Retention:* Min 30 days.
3.  **Coldline (Cold):**
    *   *Use case:* Disaster recovery (once a quarter).
    *   *Retention:* Min 90 days.
4.  **Archive (Frozen):**
    *   *Use case:* Regulatory logs (keep for 7 years). "Write once, read never."
    *   *Cost:* Tiny storage cost, HIGH access cost.
    *   *Retention:* Min 365 days.

## 4️⃣ Region vs Multi-Region Buckets
*   **Region:** Stores data in ONE place (e.g., `us-east1`). Cheaper. Good for local apps.
*   **Multi-Region:** Replicates data across a whole continent (e.g., `US` or `EU`). fast access for everyone in that country. Higher availability.

## 5️⃣ Exam Cost Traps 🚨
*   **Retrieval Fees:** If you store data in "Archive" (super cheap), it costs A LOT of money to read it back. Don't put your website images in Archive!
*   **Early Deletion Fee:** If you delete a "Coldline" file after 1 day (instead of 90 days), you are charged for the remaining 89 days anyway.
*   **Class Transitions:** You can use "Lifecycle Policies" to automatically move old files from Standard ➔ Archive to save money.

## 8️⃣ One-Line Memory Hook 🧠
> "Standard is for **Serving**; Archive is for **Hoarding**."
""",
                "hands_on_content": """## 6️⃣ Console Walkthrough
1.  **Menu:** Cloud Storage > Buckets.
2.  **Create:** Click "Create Bucket".
3.  **Name:** *Must get a green checkmark (Globally Unique).*
4.  **Location:** Choose Region or Multi-Region.
5.  **Class:** Choose "Standard" for now.
6.  **Public Access:** Uncheck "Enforce public access prevention" if you want to host a website (be careful!).
7.  **Upload:** Drag and drop a file.
""",
                "interview_questions": """## 7️⃣ Interview-Ready Q&A
**Q: "Can I host a static website on Cloud Storage?"**
*   **A:** Yes! You upload your `index.html` to a bucket, make it public, and set the "Website configuration" main page to `index.html`. It's the cheapest way to host a generic site.

**Q: "What happens if two people upload 'file.txt' at the exact same time?"**
*   **A:** The last write wins. Cloud Storage is "Strongly Consistent" for metadata, so you will immediately see the new file.
"""
            },
            {
                "number": 7,
                "title": "Week 1 Review & Mini Mock",
                "outcome": "Assess knowledge of Week 1 topics with a 10-question mock exam.",
                "description": "Recap of Foundations, Compute, and Storage + 10 questions.",
                "concept_content": """# WEEK 1 REVIEW: foundations, Compute & Storage

## 🧠 Mental Map Recap
1.  **Cloud Computing:** Renting someone else's computer (OpEx) instead of buying your own (CapEx).
2.  **Hierarchy:** Org ➔ Folders ➔ Projects ➔ Resources.
3.  **Geography:** Region (City) ➔ Zone (Building). Resources are Zonal, Regional, or Global.
4.  **Billing:** Projects pay the bills. Quotas stop you from going broke.
5.  **Compute Engine:** Virtual Machines (VMs). They are Zonal!
6.  **Storage:**
    *   **Persistent Disk:** The hard drive attached to the VM (Zonal).
    *   **Cloud Storage:** The infinite internet bucket (Global/Regional).

## 🚨 Top 3 Beginner Mistakes
1.  **The "Zone Trap":** Trying to attach a disk in `us-east1-b` to a VM in `us-east1-c`. *Impossible.*
2.  **The "Budget Myth":** Thinking a budget alert will shut down your servers. *It won't. It just emails you.*
3.  **The "Storage Class Fee":** Putting instant-access temporary files in "Archive" storage to save money, then going broke on *retrieval fees*.
""",
                "hands_on_content": """## ✅ Confidence Checklist
*   [ ] I can explain the difference between a Region and a Zone.
*   [ ] I know why we use Projects.
*   [ ] I can ssh into a VM.
*   [ ] I know when to use Standard vs Archive storage.
*   [ ] I understand that a Budget Alert is just an email, not a kill-switch.

**READY?**
If you scored 8/10 or higher, you are ready for **WEEK 2: Networking**.
*Warning: Networking is the hardest part for beginners. Rest up!*
""",
                "interview_questions": """## 📝 Mini Mock Exam (10 Questions)

**Q1. You are designing a disaster recovery plan. You need to ensure your application can survive if the entire "us-central1" region goes offline due to a hurricane. What should you do?**
*   A. Deploy resources in multiple Zones within `us-central1`.
*   B. Deploy resources in `us-central1` and `us-east1`.
*   C. Use a Preemptible VM.
*   D. Take a snapshot every hour.
> **Correct Answer: B.** *Surviving a "Region" failure requires using a second Region.* (A only survives a Zone failure).

**Q2. You have a legacy application that requires a specific version of the Linux Kernel. Which compute service should you use?**
*   A. App Engine
*   B. Cloud Run
*   C. Compute Engine
*   D. Cloud Functions
> **Correct Answer: C.** *Only Compute Engine (VMs) gives you OS-level control (Kernel, Drivers).*

**Q3. Your manager wants to view the costs of the "Marketing Department" separately from the "IT Department". Both departments are in the same Organization. What is the best way to structure this?**
*   A. Use one Project and label everything.
*   B. Use two separate Billing Accounts.
*   C. Use separate Projects for Marketing and IT, and link them to the same Billing Account.
*   D. Create a Folder for each department.
> **Correct Answer: C.** *Projects are the primary billing boundary. (D helps organize, but C is the billing answer).*

**Q4. You created a file in a Standard Storage bucket. You accessed it once, and now you won't need it for 3 years. You want to save money. What should you do?**
*   A. Leave it in Standard.
*   B. Move it to Nearline.
*   C. Move it to Coldline.
*   D. Move it to Archive.
> **Correct Answer: D.** *Archive is for data accessed less than once a year. It has the lowest storage cost.*

**Q5. A startup wants to host a simple promotional website (HTML/CSS/Images). They have $0 budget for operations and want the cheapest option. What do you recommend?**
*   A. Compute Engine (N1-standard).
*   B. Google Kubernetes Engine (GKE).
*   C. Cloud Storage (Static Website Hosting).
*   D. Cloud SQL.
> **Correct Answer: C.** *Hosting static files on Cloud Storage is significantly cheaper than running a VM (Option A) and requires zero maintenance.*

**Q6. You tried to create a new VM but received an error: `Quota Exceeded`. What does this mean?**
*   A. You ran out of money in your bank account.
*   B. You hit the hard limit of resources allowed for your project to prevent abuse.
*   C. The region is down.
*   D. You chose an invalid machine type.
> **Correct Answer: B.** *Quotas are "Hard Limits".*

**Q7. Is a Persistent Disk Zonal or Regional?**
*   A. Zonal.
*   B. Regional.
*   C. Global.
*   D. Local.
> **Correct Answer: A.** *Standard Persistent Disks reside in a single Zone.*

**Q8. Which usage type best fits a "Preemptible" VM?**
*   A. The main database for your bank.
*   B. A batch job that processes images and can resume if interrupted.
*   C. The checkout page of an e-commerce site.
*   D. A VPN server.
> **Correct Answer: B.** *Preemptible VMs can be stopped by Google at any time.*

**Q9. What is the difference between CapEx and OpEx?**
*   A. CapEx is monthly bills; OpEx is upfront cost.
*   B. CapEx is buying hardware; OpEx is renting services.
*   C. CapEx is for startups; OpEx is for enterprises.
*   D. There is no difference.
> **Correct Answer: B.** *Cloud Computing is primarily OpEx (Operational Expenditure).*

**Q10. You need to attach a GPU to your VM for machine learning. You looked in the `us-west1-a` zone but can't find the GPU type you need. What is the likely reason?**
*   A. GPUs are not supported in GCP.
*   B. Not all hardware is available in all Zones. You might need to look in `us-west1-b`.
*   C. You didn't pay enough.
*   D. You need to use a Local SSD.
> **Correct Answer: B.** *Different Zones have different hardware availability.*
"""
            }
        ]

        for day in days_data:
            d, created = Day.objects.update_or_create(
                week=week1,
                number=day['number'],
                defaults={
                    'title': day['title'],
                    'description': day['description'],
                    'outcome': day['outcome'],
                    'concept_content': day['concept_content'],
                    'hands_on_content': day['hands_on_content'],
                    'interview_questions': day['interview_questions'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created Day {day['number']}: {day['title']}"))
            else:
                self.stdout.write(f"Updated Day {day['number']}")

        self.stdout.write(self.style.SUCCESS('Successfully populated Week 1 content'))
