import os
import django
import sys
import textwrap

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def update_cloud_sql():
    # Day 10 is the original "Cloud SQL" slot. We will upgrade it to "Advanced/Core Cloud SQL".
    day = Day.objects.get(number=10)
    
    day.title = "Cloud SQL: The Core Relational DB"
    day.description = "HA, Read Replicas, and Enterprise Features."
    
    day.concept_content = textwrap.dedent("""
### 1️⃣ The Big Three Databases
In GCP, you must know when to pick what:
1.  **Cloud SQL**: MySQL/PostgreSQL/SQL Server. Regional. Good for general web apps (ERP, CRM, Wordpress).
2.  **Cloud Spanner**: **Global** Relational DB. Unlimited scale. Expensive. Good for global banking/retail.
3.  **BigQuery**: Data Warehouse. For **Analytics** (OLAP), not for running an app (OLTP).

### 2️⃣ Cloud SQL Architecture
*   **Fully Managed**: Google patches the OS and DB engine.
*   **Regional**: It lives in one region (e.g., us-central1).
*   **Storage**: Autoscaling (starts small, grows as you add data).

### 3️⃣ High Availability (HA) vs Read Replicas
This is the **#1 Exam Topic** for databases.
| Feature | **High Availability (HA)** | **Read Replica** |
| :--- | :--- | :--- |
| **Purpose** | Survival (Disaster Recovery) | Performance (Scale Reads) |
| **Setup** | Active Instance + Standby Instance (in different Zone) | Master Instance + Copy instances |
| **IP Address** | Same IP (Failover is transparent) | Different IPs |
| **Consistency** | Synchronous (Zero data loss) | Asynchronous (Lag possible) |

### 4️⃣ Connecting Securely
Never open your DB to the public internet (`0.0.0.0/0`).
*   **Private IP**: The best way. Only VMs in your VPC can connect.
*   **Cloud SQL Auth Proxy**: A secure tunnel tool provided by Google to connect from outside (or from GKE) without whitelisting IPs.
""").strip()

    day.hands_on_content = textwrap.dedent("""
### 5️⃣ Lab: Create HA MySQL Instance
1.  **Create**:
    *   Search **SQL**. Create instance **MySQL**.
    *   Edition: Enterprise or Enterprise Plus (Required for HA).
    *   *Note for Lab*: You can select "Sandbox" to save money, but note that HA options disappear.
    
2.  **Configuration**:
    *   Region: `us-central1`.
    *   **Zonal Availability**: Select **High Availability (Multiple Zones)**.
        *   Primary Zone: `us-central1-a`.
        *   Secondary Zone: `us-central1-b`.
    
3.  **Connections**:
    *   Uncheck "Public IP".
    *   Check "Private IP".
    *   Select your `global-corp-net` VPC.
    *   *Note*: It will ask to enable "Service Networking API". Do it.

4.  **Create** (Takes 10-15 mins).

5.  **Failover Test** (Mental Check):
    *   If you clicked "Failover" button, Google would flip the switch. Your app would pause for 60 seconds, then reconnect to the Secondary zone automatically.
""").strip()

    day.outcome = "architected a highly available relational database."

    day.interview_questions = textwrap.dedent("""
### 8️⃣ Interview Q&A
**Q1: Your app is reading from the DB too slowly because of high traffic. Do you enable HA or Read Replicas?**
*Answer:* Read Replicas. HA is for reliability (if the master dies). Replicas are for performance (offloading read traffic).

**Q2: Can Cloud SQL scale globally?**
*Answer:* Not really. It is a Regional service. You can have Read Replicas in other regions, but writes must go to the primary region. usage Cloud Spanner for true global horizontal scaling.

**Q3: How do you convert a Read Replica into a standalone instance?**
*Answer:* You can "Promote" a replica. This disconnects it from the master and makes it an independent writeable database. Useful for migration or testing.
""").strip()
    
    day.save()
    print(f"Updated Day 10: {day.title}")

    # Quiz
    QuizQuestion.objects.filter(day=day).delete()
    questions = [
        {
            'question_text': "Which Cloud SQL feature allows you to offload read-heavy traffic from the primary instance?",
            'option_1': "High Availability (HA)",
            'option_2': "Read Replicas",
            'option_3': "Automated Backups",
            'option_4': "SSD Storage",
            'correct_option': 2
        },
        {
            'question_text': "Cloud SQL supports which database engines?",
            'option_1': "MySQL, PostgreSQL, SQL Server",
            'option_2': "MySQL, Oracle, Aurora",
            'option_3': "Mongo, Cassandra, DynamoDB",
            'option_4': "Redis, Memcached",
            'correct_option': 1
        },
        {
            'question_text': "If you need a Relational Database that scales horizontally to unlimited size globally, what should you use?",
            'option_1': "Cloud SQL",
            'option_2': "BigQuery",
            'option_3': "Cloud Spanner",
            'option_4': "Firestore",
            'correct_option': 3
        }
    ]
    for q in questions:
        QuizQuestion.objects.create(day=day, **q)
    print(f"Created {len(questions)} quiz questions.")

if __name__ == "__main__":
    update_cloud_sql()
