from curriculum.models import Day, QuizQuestion

def convert_quiz():
    print("--- Converting Day 7 to Interactive Quiz ---")
    
    try:
        day7 = Day.objects.get(number=7)
    except Day.DoesNotExist:
        print("❌ Day 7 not found.")
        return

    # 1. Clear existing questions & static text
    print(f"Cleaning formatting for: {day7.title}")
    day7.quiz_questions.all().delete()
    day7.interview_questions = "" # Remove static text so it doesn't show twice
    day7.save()

    questions = [
        # MCQ 1
        {
            'type': 'mcq',
            'q': 'You are designing a global application for users in Japan, US, and Europe. You need a database that offers strong global consistency. Which CAP theorem attribute does GCP\'s Spanner prioritize to achieve this unique capability?',
            'o1': 'Partition Tolerance only',
            'o2': 'Availability only',
            'o3': 'Consistency and Availability (CA) - effectively',
            'o4': 'Eventual Consistency',
            'correct': 3,
            'exp': 'Spanner delivers external consistency (Consistency) and high availability (Availability) using TrueTime.'
        },
        # MCQ 2
        {
            'type': 'mcq',
            'q': 'You have a "Dev" folder and a "Prod" folder. You want to ensure NO ONE can create a VM with an external IP address in the "Prod" folder. What do you use?',
            'o1': 'IAM Role (Compute Admin)',
            'o2': 'VPC Firewall Rule',
            'o3': 'Organization Policy (Constraint)',
            'o4': 'Billing Alert',
            'correct': 3,
            'exp': 'Org Policies allow you to set strict guardrails on resources (like preventing external IPs).'
        },
        # MCQ 3
        {
            'type': 'mcq',
            'q': 'Which resource scope involves resources that survive the failure of a single data center but not a whole region?',
            'o1': 'Zonal',
            'o2': 'Regional',
            'o3': 'Multi-Regional',
            'o4': 'Global',
            'correct': 2,
            'exp': 'Regional resources are replicated across zones (data centers) within one region.'
        },
        # MCQ 4
        {
            'type': 'mcq',
            'q': 'Accessing your data in "Coldline" storage is cheaper than "Standard" storage, provided you access it less frequently than:',
            'o1': 'Once a year',
            'o2': 'Once every 90 days',
            'o3': 'Once every 30 days',
            'o4': 'Once a day',
            'correct': 2,
            'exp': 'Coldline is optimized for 90-day access cycles. (Nearline is 30 days).'
        },
        # MCQ 5
        {
            'type': 'mcq',
            'q': 'A startup wants to run a batch processing job that takes 4 hours. They want to save maximum money and can handle interruptions. Which VM type is best?',
            'o1': 'On-Demand E2',
            'o2': 'Spot VM',
            'o3': 'Committed Use Discount (1 Year)',
            'o4': 'Shielded VM',
            'correct': 2,
            'exp': 'Spot VMs offer up to 91% discounts for fault-tolerant workloads.'
        },
        # MCQ 6
        {
            'type': 'mcq',
            'q': 'You attached a "Local SSD" to your database VM for high speed. You stop the instance to resize the CPU. What happens to the Local SSD data?',
            'o1': 'It persists.',
            'o2': 'It is moved to a Persistent Disk.',
            'o3': 'It is lost (Ephemeral).',
            'o4': 'It is encrypted and saved.',
            'correct': 3,
            'exp': 'Local SSDs are physically attached and ephemeral. Stopping the VM wipes them.'
        },
        # MCQ 7
        {
            'type': 'mcq',
            'q': 'Which Identity tool is best for giving a "temporary" URL to a user to upload a file to Cloud Storage?',
            'o1': 'Service Account Key',
            'o2': 'Signed URL',
            'o3': 'IAM User',
            'o4': 'Cloud Identity',
            'correct': 2,
            'exp': 'Signed URLs are time-limited and specific, perfect for temporary access.'
        },
        # MCQ 8
        {
            'type': 'mcq',
            'q': 'What is the minimum number of zones in a standard GCP Region?',
            'o1': '1',
            'o2': '2',
            'o3': '3',
            'o4': '5',
            'correct': 3,
            'exp': 'Most regions have 3 zones (a, b, c) for high availability.'
        },
        # MCQ 9
        {
            'type': 'mcq',
            'q': 'Who pays for the resources used by a Project?',
            'o1': 'The Project Creator',
            'o2': 'The Organization Admin',
            'o3': 'The Linked Billing Account',
            'o4': 'Google',
            'correct': 3,
            'exp': 'Resources are billed to the Billing Account attached to the Project.'
        },
        # MCQ 10
        {
            'type': 'mcq',
            'q': 'Which Identifier is used by Terraform or CLI to uniquely identify your project?',
            'o1': 'Project Name',
            'o2': 'Project ID',
            'o3': 'Project Number',
            'o4': 'Organization ID',
            'correct': 2,
            'exp': 'Project ID is the unique, immutable string used in code/CLI.'
        },
        
        # --- DRILL SERGEANT (Text Questions) ---
        {
            'type': 'text',
            'q': 'Drill: A startup maps a 10TB Oracle DB requiring 100k IOPS to a Standard Persistent Disk. Why does it fail?',
            'exp': 'Standard PDs are HDD (Magnetic) and slow. They choke on high IOPS. Use Hyperdisk/Extreme PD or Local SSD.'
        },
        {
            'type': 'text',
            'q': 'Drill: "Why are we still paying IT staff if we move to cloud?" Explain TCO.',
            'exp': 'We trade CapEx (Hardware) for OpEx. IT staff moves from "unboxing servers" to "optimizing value", lowering TCO.'
        },
        {
            'type': 'text',
            'q': 'Drill: You create a VM in a new project and cannot SSH in. Why?',
            'exp': 'Implicit Deny. By default, ALL ingress traffic is blocked. You must create a firewall rule.'
        },
        {
            'type': 'text',
            'q': 'Drill: Bank requires NO data unencrypted in RAM. What feature?',
            'exp': 'Confidential VMs (uses AMD SEV to encrypt memory in use).'
        },
        {
            'type': 'text',
            'q': 'Drill: You deleted a production Folder. How long to recover?',
            'exp': '30 Days (Soft delete period).'
        }
    ]

    for item in questions:
        if item['type'] == 'mcq':
            QuizQuestion.objects.create(
                day=day7,
                question_type='mcq',
                question_text=item['q'],
                option_1=item['o1'],
                option_2=item['o2'],
                option_3=item['o3'],
                option_4=item['o4'],
                correct_option=item['correct'],
                explanation=item['exp']
            )
        else:
            QuizQuestion.objects.create(
                day=day7,
                question_type='text',
                question_text=item['q'],
                explanation=item['exp']
            )

    print(f"✅ Created {len(questions)} Interactive Quiz Questions for Day 7")

if __name__ == '__main__':
    convert_quiz()
