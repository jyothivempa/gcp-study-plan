import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def populate_quiz_part7():
    try:
        day = Day.objects.get(number=37)
    except Day.DoesNotExist:
        print("Day 37 not found.")
        return

    questions = [
        {
            "q": "You will have several applications running on different Compute Engine instances in the same project. You want to specify at a more granular level the service account each instance uses when calling Google Cloud APIs. What should you do?",
            "o1": "When creating the instances, specify the service account key for each instance.",
            "o2": "When creating the instances, specify the service account email address.",
            "o3": "Change the project's default service account.",
            "o4": "Use metadata.",
            "ans": 2
        },
        {
            "q": "You are creating an application that will run on Google Kubernetes Engine. You have identified MongoDB as the most suitable database system for your application and want to deploy a managed MongoDB environment that provides a support SLA. What should you do?",
            "o1": "Deploy MongoDB Atlas from the Google Cloud Marketplace.",
            "o2": "Install MongoDB on GKE.",
            "o3": "Use Cloud Firestore.",
            "o4": "Use Cloud Bigtable.",
            "ans": 1
        },
        {
            "q": "You are managing a project for the Business Intelligence (BI) department in your company. A data pipeline ingests data into BigQuery via streaming. You want the users in the BI department to be able to run the custom SQL queries against the latest data in BigQuery. What should you do?",
            "o1": "Use BigQuery (native support for real-time analysis).",
            "o2": "Export to Cloud Storage CSV.",
            "o3": "Use Dataflow.",
            "o4": "Use Dataproc.",
            "ans": 1
        },
        {
            "q": "Your company is moving its entire workload to Compute Engine. Some servers should be accessible through the Internet, and other servers should only be accessible over the internal network. All servers need to be able to talk to each other over specific ports and protocols. The current on-premises network relies on a demilitarized zone (DMZ) for the public servers and a Local Area Network (LAN) for the private servers. You need to design the networking infrastructure on Google Cloud to match these requirements. What should you do?",
            "o1": "Use a single VPC configuration with appropriate firewall rules (using tags/service accounts) and subnets.",
            "o2": "Create 2 VPCs and Peer them.",
            "o3": "Use Legacy Networks.",
            "o4": "Use multiple Projects.",
            "ans": 1
        }
    ]

    for q in questions:
        QuizQuestion.objects.create(
            day=day,
            question_text=q['q'],
            option_1=q['o1'],
            option_2=q['o2'],
            option_3=q['o3'],
            option_4=q['o4'],
            correct_option=q['ans']
        )
    
    print(f"Successfully populated {len(questions)} questions for Day 31 (Part 7 - Final).")

if __name__ == "__main__":
    populate_quiz_part7()
