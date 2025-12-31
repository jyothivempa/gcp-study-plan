import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def update_day21_quiz():
    day_num = 21
    try:
        day = Day.objects.get(number=day_num)
    except Day.DoesNotExist:
        print(f"Day {day_num} not found!")
        return

    # Clear existing questions to avoid duplicates
    QuizQuestion.objects.filter(day=day).delete()
    print(f"Cleared existing questions for Day {day_num}.")

    questions = [
        {
            "q": "You need to give a consultant read-only access to a specific Cloud Storage bucket. You do not want them to see anything else in the project. What should you do?",
            "o1": "Assign roles/viewer at the Project level.",
            "o2": "Assign roles/storage.objectViewer at the Bucket level.",
            "o3": "Create a Service Account for them.",
            "o4": "Assign roles/owner at the Bucket level.",
            "ans": 2
        },
        {
            "q": "Your application running on a VM needs to write data to BigQuery. What is the most secure method to authenticate?",
            "o1": "Embed a Service Account JSON key in the source code.",
            "o2": "Store the JSON key in a text file on the VM.",
            "o3": "Create a Service Account with the BigQuery Data Editor role and attach it to the VM.",
            "o4": "Use your personal Gmail account credentials.",
            "ans": 3
        },
        {
            "q": "You want to receive an email notification whenever a specific error message appears in your application logs. Which tool should you use?",
            "o1": "Cloud Monitoring (Alerting Policy) based on a Log-based Metric.",
            "o2": "Cloud Trace.",
            "o3": "Cloud Profiler.",
            "o4": "VPC Flow Logs.",
            "ans": 1
        },
        {
            "q": "Who is responsible for securing the underlying physical hardware of the data center?",
            "o1": "You (The Customer).",
            "o2": "Google.",
            "o3": "Both (Shared Responsibility).",
            "o4": "The ISP.",
            "ans": 2
        },
        {
            "q": "A user left your company. You deleted their Google Account. What happens to the IAM policies that referenced that user?",
            "o1": "They act as 'orphaned' entries but effectively deny access.",
            "o2": "The policies are automatically deleted.",
            "o3": "The Project is suspended.",
            "o4": "The user can still log in.",
            "ans": 1
        },
        {
            "q": "Which command would you use to list all the VMs in your project?",
            "o1": "gcloud compute instances list",
            "o2": "gcloud vm show",
            "o3": "kubectl get pods",
            "o4": "gsutil ls",
            "ans": 1
        },
        {
            "q": "You need to store audit logs for 7 years to meet compliance regulations. What should you do?",
            "o1": "Do nothing; Cloud Logging keeps them forever.",
            "o2": "Create a Log Sink to export logs to a Cloud Storage bucket with an Archive lifecycle policy.",
            "o3": "Print them out.",
            "o4": "Export them to BigQuery.",
            "ans": 2
        },
        {
            "q": "What is the difference between a Role and a Permission?",
            "o1": "They are the same.",
            "o2": "A Role contains many Permissions. You assign Roles to users.",
            "o3": "A Permission contains many Roles.",
            "o4": "Permissions are for users; Roles are for robots.",
            "ans": 2
        },
        {
            "q": "Provide the CLI command to initialize the configuration (login, set project/region).",
            "o1": "gcloud start",
            "o2": "gcloud login",
            "o3": "gcloud init",
            "o4": "gcloud config set",
            "ans": 3
        },
        {
            "q": "Can you restrict an IAM Role to be active only during working hours (e.g., 9 AM to 5 PM)?",
            "o1": "No, IAM is permanent.",
            "o2": "Yes, using IAM Conditions.",
            "o3": "Only for Billing roles.",
            "o4": "Yes, by using a cron job to delete the user every night.",
            "ans": 2
        }
    ]

    for q_data in questions:
        QuizQuestion.objects.create(
            day=day,
            question_text=q_data["q"],
            option_1=q_data["o1"],
            option_2=q_data["o2"],
            option_3=q_data["o3"],
            option_4=q_data["o4"],
            correct_option=q_data["ans"]
        )
    
    print(f"Successfully added {len(questions)} quiz questions to Day 21.")

if __name__ == "__main__":
    update_day21_quiz()
