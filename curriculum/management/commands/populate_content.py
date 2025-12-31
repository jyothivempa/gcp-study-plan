from django.core.management.base import BaseCommand
from curriculum.models import Week, Day, QuizQuestion
from .content_data import DAYS_CONTENT
import textwrap

class Command(BaseCommand):
    help = 'Populates the database with 30 days of GCP content'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting content population...')

        # 1. Create Weeks
        weeks_data = [
            {'number': 1, 'description': 'Cloud Fundamentals & Core Infrastructure'},
            {'number': 2, 'description': 'Storage, Databases & Networking Deep Dive'},
            {'number': 3, 'description': 'Security, Identity & Monitoring'},
            {'number': 4, 'description': 'Containerization, Serverless & Final Prep'},
        ]

        for w_data in weeks_data:
            Week.objects.get_or_create(number=w_data['number'], defaults={'description': w_data['description']})
        
        self.stdout.write('Weeks created.')

        # 2. Define Day 1 (Detailed)
        day1_content = {
            'number': 1,
            'title': 'Welcome to Google Cloud Platform',
            'week_num': 1,
            'description': 'Understand the basics of Cloud Computing and tour the console.',
            'concept': """
### 1️⃣ Plain-English Explanation
**The Cloud = Someone Else's Computer That You Rent**

Imagine you want to host a dinner party. You have two options:
*   **OLD WAY (On-Premise)**: You buy your own kitchen, stove, plates, chairs, tables, hire staff. You own everything. If you throw 3 parties a year, the rest of the time your expensive kitchen sits empty. If your stove breaks, you fix it.
*   **NEW WAY (Cloud)**: You rent a party hall from a company. They have kitchens, plates, chairs, staff. You pay only when you use it. If you need more tables for 500 people, the hall provides them.

### 2️⃣ Real-World Analogy: Electricity Supply
You don't own the power plant that makes your electricity.
*   **Old way**: Build your own power generator, maintain it, buy fuel.
*   **Modern way**: Plug into the grid, use electricity when you need it, pay the bill.
*   **Cloud** is the same. Instead of owning servers, you "plug into" Google's servers.

### 3️⃣ Why Cloud Exists (Exam Focus)
| Problem | Without Cloud | With Cloud |
| :--- | :--- | :--- |
| **Cost** | Buy expensive servers upfront (CapEx) | Pay as you go (OpEx) |
| **Usage** | Idle 70% of the time | Scale up/down instantly |
| **Maintenance** | You fix broken hardware | Google fixes it |

### 4️⃣ How Cloud Works
**Three simple layers:**
1.  **YOU**: Your business apps, websites.
2.  **GOOGLE'S INFRASTRUCTURE**: Servers, storage, networking.
3.  **GOOGLE'S DATA CENTERS**: Physical buildings with computers.

### 6️⃣ Exam Triggers 🚨
*   **"On-Premise"**: You own the servers physically.
*   **"Scalability"**: Ability to handle more load ("Scale up on Black Friday").
*   **"CapEx vs OpEx"**:
    *   *CapEx*: Upfront cost to buy (Owning a house).
    *   *OpEx*: Recurring operating cost (Renting a house).
*   **"Latency"**: How fast data travels (Choose a region close to users).

### 9️⃣ One-Line Memory Hook 🧠
**Cloud = Plug into Google's electricity grid for computing power instead of building your own power plant.**
""",
            'hands_on': """
### 5️⃣ GCP Console Walkthrough (STEP-BY-STEP)

**Step 1: Access Google Cloud Console**
1.  Go to: [console.cloud.google.com](https://console.cloud.google.com).
2.  Sign in with your Google account.

**Step 2: Create a Project (Your Sandbox)**
1.  Click the **Project Dropdown** (top left, blue bar).
2.  Click **New Project**.
3.  Name it: `My-First-Cloud`.
4.  Click **Create**.
    *   *What just happened?* You created a logical container in Google's infrastructure that's yours.

**Step 3: Enable Billing**
1.  Click **Billing** in the left menu (Hamburger icon).
2.  Follow prompts to link an account.
    *   *Note*: Google gives a $300 free credit. You aren't charged unless you upgrade.
""",
            'outcome': 'mastered the fundamental concepts of Cloud Computing.',
            'interview_qs': """
### 8️⃣ Interview-Ready Q&A
**Q1: What is cloud computing in one sentence?**
*Answer:* Cloud computing is renting computing power and storage from a provider instead of buying and managing your own servers.

**Q2: What is the main advantage of cloud for a startup?**
*Answer:* Low barrier to entry. They can start with tiny costs (OpEx) and grow without buying expensive servers upfront (CapEx).

**Q3: Is cloud always cheaper?**
*Answer:* Not always. If you have a constant, predictable workload 24/7, buying your own hardware can sometimes be cheaper long-term.
"""
        }

        # 3. Create List of 30 Days from Imported Data
        days_list = [day1_content]

        for num, data in DAYS_CONTENT.items():
            # Determine Week based on ranges (approx)
            if 2 <= num <= 7: week_num = 1
            elif 8 <= num <= 14: week_num = 2
            elif 15 <= num <= 21: week_num = 3
            else: week_num = 4

            days_list.append({
                'number': num,
                'week_num': week_num,
                'title': data['title'],
                'description': data['description'],
                'concept': data['concept'],
                'hands_on': data['hands_on'],
                'outcome': data['outcome'],
                'interview_qs': data['interview_qs']
            })

        # 4. Save to DB
        for d in days_list:
            week = Week.objects.get(number=d['week_num'])
            
            # Clean using textwrap.dedent to remove indentation issues for Mermaid/Markdown
            clean_concept = textwrap.dedent(d['concept']).strip() if d['concept'] else ""
            clean_hands_on = textwrap.dedent(d['hands_on']).strip() if d['hands_on'] else ""
            clean_interview = textwrap.dedent(d['interview_qs']).strip() if d.get('interview_qs') else ""

            Day.objects.update_or_create(
                number=d['number'],
                defaults={
                    'week': week,
                    'title': d['title'],
                    'description': d['description'],
                    'concept_content': clean_concept,
                    'hands_on_content': clean_hands_on,
                    'outcome': d['outcome'],
                    'interview_questions': clean_interview
                }
            )

        # 5. Quiz for Day 1
        day1 = Day.objects.get(number=1)
        
        # Always clear and recreate questions to ensure they are up to date
        QuizQuestion.objects.filter(day=day1).delete()
        
        questions = [
            {
                'question_text': "Which GCP service model would you use if you want to rent raw Virtual Machines (VMs)?",
                'option_1': "SaaS (Software as a Service)",
                'option_2': "PaaS (Platform as a Service)",
                'option_3': "IaaS (Infrastructure as a Service)",
                'option_4': "FaaS (Function as a Service)",
                'correct_option': 3
            },
            {
                'question_text': "Where in the GCP Console can you manage permissions and access control?",
                'option_1': "Compute Engine",
                'option_2': "IAM & Admin",
                'option_3': "Cloud Storage",
                'option_4': "VPC Network",
                'correct_option': 2
            },
            {
                'question_text': "Which analogy best describes Cloud Computing compared to On-Premise?",
                'option_1': "Owning a car vs. Renting a taxi/Uber",
                'option_2': "Buying a house vs. Building a house",
                'option_3': "Cooking at home vs. Cooking at a friend's house",
                'option_4': "None of the above",
                'correct_option': 1
            }
        ]

        for q in questions:
            QuizQuestion.objects.create(day=day1, **q)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated 30 days of content.'))
