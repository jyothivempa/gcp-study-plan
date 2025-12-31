from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from curriculum.models import Day, Week, UserProgress

User = get_user_model()

class CurriculumViewTests(TestCase):
    def setUp(self):
        # Create user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()
        
        # Create Week and Day
        self.week = Week.objects.create(number=1, description="Fundamentals")
        self.day = Day.objects.create(
            week=self.week, 
            number=1, 
            title="Intro to GCP", 
            description="Basics",
            concept_content="Concept",
            hands_on_content="Hands on"
        )

    def test_home_page_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_curriculum_overview_loads(self):
        response = self.client.get(reverse('curriculum_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Intro to GCP")

    def test_lesson_detail_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('lesson_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Intro to GCP")

    def test_progress_tracking(self):
        self.client.login(username='testuser', password='password123')
        # Simulate completing a lesson
        UserProgress.objects.create(user=self.user, day=self.day, completed=True)
        
        response = self.client.get(reverse('curriculum_overview'))
        # Check if the context contains the completed day ID
        self.assertIn(self.day.id, response.context['completed_day_ids'])

    def test_quiz_rendering(self):
        self.client.login(username='testuser', password='password123')
        # Create a quiz question for the day
        from curriculum.models import QuizQuestion
        QuizQuestion.objects.create(
            day=self.day,
            question_text="What is Cloud Computing?",
            option_1="Renting resources",
            option_2="Buying hardware",
            correct_option=1
        )
        
        response = self.client.get(reverse('lesson_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "What is Cloud Computing?")
        self.assertContains(response, "Renting resources")

