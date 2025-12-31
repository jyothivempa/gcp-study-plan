import os
import django
import sys
import textwrap

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day, QuizQuestion

def update_cloud_run():
    day = Day.objects.get(number=25)
    
    day.title = "Cloud Run (Serverless Containers)"
    day.description = "Deploy Any Container, Scale to Zero."
    
    day.concept_content = textwrap.dedent("""
### 1️⃣ Plain-English Explanation
**Cloud Run** is the "Goldilocks" service of GCP.
*   **GKE** is powerful but complex (Manage clusters, nodes).
*   **App Engine** is easy but restrictive (Specific languages).
*   **Cloud Run** is perfect: You give it a **Docker Container** (so you can run any language/binary), and Google runs it **Serverlessly** (no nodes to manage, scales to zero).

### 2️⃣ How it works: Knative
It's built on an open-source standard called **Knative**. This means you aren't locked in forever; you could move your workload to any Kubernetes cluster later.

### 3️⃣ Key Features (Exam Focus)
1.  **Stateless**: Your app cannot save files to its own hard drive (it disappears when the container stops). You must save files to **Cloud Storage** or **Cloud SQL**.
2.  **Concurrency**: Unlike Cloud Functions (which handles 1 request per instance), one Cloud Run container can handle **80 concurrent requests** (configurable up to 1000). This makes it much cheaper for high-traffic apps.
3.  **Scale to Zero**: If no one visits your site at 3 AM, you pay **$0.00**.

### 4️⃣ Traffic Splitting (Canary)
You can deploy `v2` of your app and tell Cloud Run: "Send 10% of users to v2, and 90% to v1". If v2 crashes, you just revert the dial. No downtime.
""").strip()

    day.hands_on_content = textwrap.dedent("""
### 5️⃣ Console Walkthrough: Deploy & Split Traffic
**Goal**: Deploy a container and perform a split traffic update.

1.  **Deploy V1**:
    *   Search **Cloud Run**. Click **Create Service**.
    *   Container URL: `us-docker.pkg.dev/cloudrun/container/hello` (Google's demo).
    *   Service Name: `frontend`.
    *   Region: `us-central1`.
    *   **Authentication**: Allow unauthenticated invocations (Public).
    *   Click **Create**.
    *   *Result*: A green URL. Open it (It says "It's running!").

2.  **Deploy V2 (The Canary)**:
    *   Click **Edit & Deploy New Revision**.
    *   Change something (e.g., Environment Variable `COLOR=RED` or just redeploy).
    *   Click **Deploy**.

3.  **Split Traffic**:
    *   Go to the **Revisions** tab.
    *   Click **Manage Traffic**.
    *   Set **Revision 1** to 50% and **Revision 2** to 50%.
    *   Save.
    *   Refresh your URL multiple times. You will bounce between versions!
""").strip()

    day.outcome = "performed a canary deployment using Cloud Run."

    day.interview_questions = textwrap.dedent("""
### 8️⃣ Interview Q&A
**Q1: What is the difference between Cloud Run and Cloud Functions?**
*Answer:* Cloud Functions is "Function-as-a-Service" (snippets of code, limited runtimes). Cloud Run is "Container-as-a-Service" (any binary, custom OS libraries). Cloud Run also handles higher concurrency per instance.

**Q2: Can I run a background worker data processing job on Cloud Run?**
*Answer:* Yes, using **Cloud Run Jobs** (a relatively new feature distinct from Cloud Run Services). It runs to completion and then exits, rather than waiting for HTTP requests.

**Q3: How do you secure a private Cloud Run service?**
*Answer:* Set "Require Encryption" (No allow unauthenticated). Then, only users/services with the `Cloud Run Invoker` IAM role can call it.
""").strip()
    
    day.save()
    print(f"Updated Day 25: {day.title}")

    # Quiz
    QuizQuestion.objects.filter(day=day).delete()
    questions = [
        {
            'question_text': "What happens to a Cloud Run service when no requests are coming in?",
            'option_1': "It runs 1 instance constantly on standby",
            'option_2': "It scales to zero instances (Costing $0)",
            'option_3': "It shuts down but charges for storage",
            'option_4': "It pauses and requires a manual restart",
            'correct_option': 2
        },
        {
            'question_text': "Cloud Run is built on which open-source standard?",
            'option_1': "Docker Swarm",
            'option_2': "Knative",
            'option_3': "Terraform",
            'option_4': "OpenStack",
            'correct_option': 2
        },
        {
            'question_text': "Which feature allows you to safely test a new version of your app on a subset of users?",
            'option_1': "Load Balancing",
            'option_2': "Traffic Splitting",
            'option_3': "Auto-healing",
            'option_4': "Circuit Breaker",
            'correct_option': 2
        }
    ]
    for q in questions:
        QuizQuestion.objects.create(day=day, **q)
    print(f"Created {len(questions)} quiz questions.")

if __name__ == "__main__":
    update_cloud_run()
