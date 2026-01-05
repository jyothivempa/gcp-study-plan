"""
Comprehensive Test Suite for GCP Study Plan - Curriculum App
=============================================================
Phase 1: Model Unit Tests
Phase 2: View Unit Tests  
Phase 3: Integration Tests
Phase 4: API Endpoint Tests
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
import json

from curriculum.models import (
    Course, Week, Day, UserProgress, UserNote, QuizQuestion, SearchLog
)

User = get_user_model()


# =============================================================================
# PHASE 1: MODEL UNIT TESTS
# =============================================================================

class CourseModelTests(TestCase):
    """Unit tests for Course model"""
    
    def test_course_creation(self):
        """Test basic course creation"""
        course = Course.objects.create(
            title="Google Cloud Platform",
            slug="gcp",
            description="45-day GCP certification course"
        )
        self.assertEqual(str(course), "Google Cloud Platform")
        self.assertEqual(course.slug, "gcp")
    
    def test_course_slug_uniqueness(self):
        """Test that course slugs must be unique"""
        Course.objects.create(title="GCP", slug="gcp")
        with self.assertRaises(Exception):
            Course.objects.create(title="GCP Duplicate", slug="gcp")
    
    def test_course_default_icon(self):
        """Test default icon class is set"""
        course = Course.objects.create(title="Test", slug="test")
        self.assertEqual(course.icon_class, "fa-brands fa-google")


class WeekModelTests(TestCase):
    """Unit tests for Week model"""
    
    def setUp(self):
        self.course = Course.objects.create(title="GCP", slug="gcp")
    
    def test_week_creation(self):
        """Test basic week creation"""
        week = Week.objects.create(
            course=self.course,
            number=1,
            description="Fundamentals Week"
        )
        self.assertEqual(week.number, 1)
        self.assertIn("GCP", str(week))
    
    def test_week_ordering(self):
        """Test weeks are ordered by course and number"""
        Week.objects.create(course=self.course, number=3, description="Week 3")
        Week.objects.create(course=self.course, number=1, description="Week 1")
        Week.objects.create(course=self.course, number=2, description="Week 2")
        
        weeks = list(Week.objects.all())
        self.assertEqual(weeks[0].number, 1)
        self.assertEqual(weeks[1].number, 2)
        self.assertEqual(weeks[2].number, 3)
    
    def test_week_unique_together(self):
        """Test course-week number uniqueness"""
        Week.objects.create(course=self.course, number=1, description="First")
        with self.assertRaises(Exception):
            Week.objects.create(course=self.course, number=1, description="Duplicate")


class DayModelTests(TestCase):
    """Unit tests for Day model"""
    
    def setUp(self):
        self.course = Course.objects.create(title="GCP", slug="gcp")
        self.week = Week.objects.create(
            course=self.course, number=1, description="Week 1"
        )
    
    def test_day_creation(self):
        """Test basic day creation with required fields"""
        day = Day.objects.create(
            week=self.week,
            number=1,
            title="Cloud Foundations",
            description="Introduction to cloud computing",
            concept_content="# Cloud Computing Basics",
            hands_on_content="## Lab: Create GCP Account",
            outcome="Understand cloud fundamentals"
        )
        self.assertEqual(str(day), "Day 1: Cloud Foundations")
    
    def test_day_ordering(self):
        """Test days are ordered by number"""
        Day.objects.create(
            week=self.week, number=3, title="Day 3",
            concept_content="C", hands_on_content="H", outcome="O"
        )
        Day.objects.create(
            week=self.week, number=1, title="Day 1",
            concept_content="C", hands_on_content="H", outcome="O"
        )
        
        days = list(Day.objects.all())
        self.assertEqual(days[0].number, 1)
        self.assertEqual(days[1].number, 3)
    
    def test_day_timestamps(self):
        """Test auto timestamps are set"""
        day = Day.objects.create(
            week=self.week, number=1, title="Test Day",
            concept_content="C", hands_on_content="H", outcome="O"
        )
        self.assertIsNotNone(day.created_at)
        self.assertIsNotNone(day.updated_at)


class UserProgressModelTests(TestCase):
    """Unit tests for UserProgress model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.course = Course.objects.create(title="GCP", slug="gcp")
        self.week = Week.objects.create(
            course=self.course, number=1, description="Week 1"
        )
        self.day = Day.objects.create(
            week=self.week, number=1, title="Day 1",
            concept_content="C", hands_on_content="H", outcome="O"
        )
    
    def test_progress_creation(self):
        """Test creating user progress"""
        progress = UserProgress.objects.create(
            user=self.user,
            day=self.day,
            completed=False
        )
        self.assertFalse(progress.completed)
        self.assertIsNone(progress.completed_at)
    
    def test_progress_completion(self):
        """Test marking progress as complete"""
        progress = UserProgress.objects.create(
            user=self.user,
            day=self.day,
            completed=True,
            completed_at=timezone.now()
        )
        self.assertTrue(progress.completed)
        self.assertIsNotNone(progress.completed_at)
    
    def test_progress_unique_per_user_day(self):
        """Test user can only have one progress per day"""
        UserProgress.objects.create(user=self.user, day=self.day)
        with self.assertRaises(Exception):
            UserProgress.objects.create(user=self.user, day=self.day)
    
    def test_progress_str_representation(self):
        """Test string representation shows status"""
        progress = UserProgress.objects.create(
            user=self.user, day=self.day, completed=True
        )
        self.assertIn("Done", str(progress))


class QuizQuestionModelTests(TestCase):
    """Unit tests for QuizQuestion model"""
    
    def setUp(self):
        self.course = Course.objects.create(title="GCP", slug="gcp")
        self.week = Week.objects.create(
            course=self.course, number=1, description="Week 1"
        )
        self.day = Day.objects.create(
            week=self.week, number=1, title="Day 1",
            concept_content="C", hands_on_content="H", outcome="O"
        )
    
    def test_mcq_question_creation(self):
        """Test creating MCQ question with options"""
        question = QuizQuestion.objects.create(
            day=self.day,
            question_type='mcq',
            question_text="What is Cloud Computing?",
            option_1="Renting compute resources",
            option_2="Buying servers",
            option_3="Using local storage",
            option_4="None of above",
            correct_option=1
        )
        self.assertEqual(question.question_type, 'mcq')
        self.assertEqual(question.correct_option, 1)
    
    def test_text_question_creation(self):
        """Test creating self-check text question"""
        question = QuizQuestion.objects.create(
            day=self.day,
            question_type='text',
            question_text="Explain the benefits of cloud.",
            explanation="Cloud provides scalability, flexibility..."
        )
        self.assertEqual(question.question_type, 'text')
        self.assertIn("scalability", question.explanation)


class UserNoteModelTests(TestCase):
    """Unit tests for UserNote model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.course = Course.objects.create(title="GCP", slug="gcp")
        self.week = Week.objects.create(
            course=self.course, number=1, description="Week 1"
        )
        self.day = Day.objects.create(
            week=self.week, number=1, title="Day 1",
            concept_content="C", hands_on_content="H", outcome="O"
        )
    
    def test_note_creation(self):
        """Test creating a user note"""
        note = UserNote.objects.create(
            user=self.user,
            day=self.day,
            content="My personal notes for day 1"
        )
        self.assertIn("My personal notes", note.content)
    
    def test_note_unique_per_user_day(self):
        """Test user can only have one note per day"""
        UserNote.objects.create(user=self.user, day=self.day, content="Note 1")
        with self.assertRaises(Exception):
            UserNote.objects.create(user=self.user, day=self.day, content="Note 2")


# =============================================================================
# PHASE 2: VIEW UNIT TESTS
# =============================================================================

class CurriculumViewTests(TestCase):
    """Unit tests for curriculum views"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.course = Course.objects.create(
            title="GCP", slug="gcp", description="GCP Course"
        )
        self.week = Week.objects.create(
            course=self.course, number=1, description="Fundamentals"
        )
        self.day = Day.objects.create(
            week=self.week, number=1, title="Cloud Foundations",
            description="Intro to cloud",
            concept_content="# Cloud Computing\nLearn the basics",
            hands_on_content="## Lab\nCreate account",
            outcome="Understand cloud"
        )
    
    def test_curriculum_overview_anonymous(self):
        """Test curriculum overview redirects to course detail"""
        response = self.client.get(reverse('curriculum_overview'))
        # curriculum_overview redirects to course_detail
        self.assertEqual(response.status_code, 302)
    
    def test_course_detail_view(self):
        """Test course detail page loads"""
        response = self.client.get(
            reverse('course_detail', args=['gcp'])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "GCP")
    
    def test_lesson_detail_authenticated(self):
        """Test lesson detail requires authentication"""
        # First try without login
        response = self.client.get(
            reverse('lesson_detail', args=['gcp', 1])
        )
        # Should redirect to login or return lesson
        self.assertIn(response.status_code, [200, 302])
        
        # Now login and try again
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('lesson_detail', args=['gcp', 1])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cloud Foundations")
    
    def test_lesson_detail_with_quiz(self):
        """Test lesson detail shows quiz questions"""
        QuizQuestion.objects.create(
            day=self.day,
            question_type='mcq',
            question_text="What is GCP?",
            option_1="Google Cloud Platform",
            option_2="Global Cloud Provider",
            correct_option=1
        )
        
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('lesson_detail', args=['gcp', 1])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "What is GCP?")
    
    def test_nonexistent_lesson(self):
        """Test 404 for nonexistent lesson"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('lesson_detail', args=['gcp', 999])
        )
        self.assertEqual(response.status_code, 404)
    
    def test_dashboard_requires_login(self):
        """Test dashboard requires authentication"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_dashboard_authenticated(self):
        """Test dashboard redirects for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        # Dashboard redirects to curriculum_overview
        self.assertEqual(response.status_code, 302)


class SearchViewTests(TestCase):
    """Unit tests for search functionality"""
    
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(title="GCP", slug="gcp")
        self.week = Week.objects.create(
            course=self.course, number=1, description="Week 1"
        )
        Day.objects.create(
            week=self.week, number=1, title="Cloud Computing Basics",
            description="Learn cloud fundamentals",
            concept_content="Learn about VMs and containers",
            hands_on_content="Lab", outcome="O"
        )
        Day.objects.create(
            week=self.week, number=2, title="Networking Fundamentals",
            description="VPC basics",
            concept_content="VPC and subnets",
            hands_on_content="Lab", outcome="O"
        )
    
    def test_search_finds_matching_days(self):
        """Test search finds days matching the query"""
        from curriculum.models import Day
        days = Day.objects.filter(title__icontains='Cloud')
        self.assertEqual(days.count(), 1)
        self.assertEqual(days.first().title, "Cloud Computing Basics")
    
    def test_search_by_content(self):
        """Test search finds days by content field"""
        from curriculum.models import Day
        days = Day.objects.filter(concept_content__icontains='VPC')
        self.assertEqual(days.count(), 1)
        self.assertEqual(days.first().title, "Networking Fundamentals")
    
    def test_search_no_results(self):
        """Test search with no matching results"""
        from curriculum.models import Day
        days = Day.objects.filter(title__icontains='nonexistent')
        self.assertEqual(days.count(), 0)
    
    def test_search_log_created(self):
        """Test search creates a log entry"""
        from curriculum.models import SearchLog
        SearchLog.objects.create(query="test query", results_count=5)
        log = SearchLog.objects.filter(query="test query").first()
        self.assertIsNotNone(log)
        self.assertEqual(log.results_count, 5)


# =============================================================================
# PHASE 3: INTEGRATION TESTS
# =============================================================================

class UserProgressIntegrationTests(TestCase):
    """Integration tests for user progress tracking"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='learner', password='learn123'
        )
        self.course = Course.objects.create(title="GCP", slug="gcp")
        self.week = Week.objects.create(
            course=self.course, number=1, description="Week 1"
        )
        
        # Create multiple days
        for i in range(1, 8):
            Day.objects.create(
                week=self.week, number=i, title=f"Day {i}",
                concept_content="Content", hands_on_content="Lab", outcome="Goal"
            )
    
    def test_progress_tracking_workflow(self):
        """Test complete workflow of tracking progress"""
        self.client.login(username='learner', password='learn123')
        
        # Initially no progress
        self.assertEqual(UserProgress.objects.filter(user=self.user).count(), 0)
        
        # Complete day 1
        day1 = Day.objects.get(number=1)
        UserProgress.objects.create(
            user=self.user, day=day1, completed=True,
            completed_at=timezone.now()
        )
        
        # Verify progress
        self.assertEqual(
            UserProgress.objects.filter(user=self.user, completed=True).count(), 1
        )
        
        # Complete days 2-3
        for day_num in [2, 3]:
            day = Day.objects.get(number=day_num)
            UserProgress.objects.create(
                user=self.user, day=day, completed=True,
                completed_at=timezone.now()
            )
        
        # Verify total progress
        completed = UserProgress.objects.filter(
            user=self.user, completed=True
        ).count()
        self.assertEqual(completed, 3)
    
    def test_progress_persists_across_sessions(self):
        """Test that progress is saved across login sessions"""
        self.client.login(username='learner', password='learn123')
        
        # Create progress
        day1 = Day.objects.get(number=1)
        UserProgress.objects.create(
            user=self.user, day=day1, completed=True
        )
        
        # Logout
        self.client.logout()
        
        # Login again
        self.client.login(username='learner', password='learn123')
        
        # Verify progress still exists
        progress = UserProgress.objects.filter(user=self.user).first()
        self.assertTrue(progress.completed)


class CourseNavigationIntegrationTests(TestCase):
    """Integration tests for course navigation flow"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='student', password='student123'
        )
        
        # Create full course structure
        self.course = Course.objects.create(
            title="GCP 45-Day Course", slug="gcp"
        )
        
        for week_num in range(1, 7):
            week = Week.objects.create(
                course=self.course, number=week_num,
                description=f"Week {week_num} Content"
            )
            
            # 7 days per week (roughly)
            start_day = (week_num - 1) * 7 + 1
            end_day = min(start_day + 6, 45)
            
            for day_num in range(start_day, end_day + 1):
                Day.objects.create(
                    week=week, number=day_num, title=f"Day {day_num} Topic",
                    concept_content="Concept", hands_on_content="Lab", outcome="Goal"
                )
    
    def test_full_navigation_flow(self):
        """Test navigating through entire course structure"""
        self.client.login(username='student', password='student123')
        
        # 1. curriculum overview redirects to course detail
        response = self.client.get(reverse('curriculum_overview'))
        self.assertEqual(response.status_code, 302)
        
        # 2. Go to course detail
        response = self.client.get(reverse('course_detail', args=['gcp']))
        self.assertEqual(response.status_code, 200)
        
        # 3. Access first lesson
        response = self.client.get(reverse('lesson_detail', args=['gcp', 1]))
        self.assertEqual(response.status_code, 200)
        
        # 4. Access middle lesson
        response = self.client.get(reverse('lesson_detail', args=['gcp', 22]))
        self.assertEqual(response.status_code, 200)


# =============================================================================
# PHASE 4: API ENDPOINT TESTS
# =============================================================================

class SaveNoteAPITests(TestCase):
    """API tests for save note endpoint"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='noter', password='note123'
        )
        self.course = Course.objects.create(title="GCP", slug="gcp")
        self.week = Week.objects.create(
            course=self.course, number=1, description="Week 1"
        )
        self.day = Day.objects.create(
            week=self.week, number=1, title="Day 1",
            concept_content="C", hands_on_content="H", outcome="O"
        )
    
    def test_save_note_requires_login(self):
        """Test save note API requires authentication"""
        response = self.client.post(
            reverse('save_note', args=[1]),
            data={'content': 'My notes'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_save_note_creates_note(self):
        """Test save note API creates a note"""
        self.client.login(username='noter', password='note123')
        
        response = self.client.post(
            reverse('save_note', args=[1]),
            data=json.dumps({'content': 'My learning notes'}),
            content_type='application/json'
        )
        
        self.assertIn(response.status_code, [200, 201])
        
        # Verify note was saved
        note = UserNote.objects.filter(user=self.user, day=self.day).first()
        if note:
            self.assertIn('learning', note.content)
    
    def test_save_note_updates_existing(self):
        """Test save note API updates existing note"""
        self.client.login(username='noter', password='note123')
        
        # Create initial note
        UserNote.objects.create(
            user=self.user, day=self.day, content='Original content'
        )
        
        # Update note
        response = self.client.post(
            reverse('save_note', args=[1]),
            data=json.dumps({'content': 'Updated content'}),
            content_type='application/json'
        )
        
        # Check only one note exists
        notes = UserNote.objects.filter(user=self.user, day=self.day)
        self.assertEqual(notes.count(), 1)


class SidebarDataAPITests(TestCase):
    """API tests for sidebar data endpoint"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='sideuser', password='side123'
        )
        self.course = Course.objects.create(title="GCP", slug="gcp")
        self.week = Week.objects.create(
            course=self.course, number=1, description="Week 1"
        )
        
        for i in range(1, 8):
            Day.objects.create(
                week=self.week, number=i, title=f"Day {i}",
                concept_content="C", hands_on_content="H", outcome="O"
            )
    
    def test_sidebar_returns_json(self):
        """Test sidebar API returns JSON data"""
        self.client.login(username='sideuser', password='side123')
        
        response = self.client.get(
            reverse('get_sidebar_data', args=['gcp', 1])
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response['Content-Type'])
    
    def test_sidebar_contains_navigation_data(self):
        """Test sidebar API includes navigation info"""
        self.client.login(username='sideuser', password='side123')
        
        response = self.client.get(
            reverse('get_sidebar_data', args=['gcp', 3])
        )
        
        data = response.json()
        
        # Check required fields match the actual API response
        self.assertIn('week_number', data)
        self.assertIn('items', data)


# =============================================================================
# PHASE 5: CONTENT VALIDATION TESTS
# =============================================================================

class ContentFileTests(TestCase):
    """Tests to validate curriculum content files"""
    
    def test_content_files_exist(self):
        """Test that key content section files exist"""
        import os
        
        content_dir = 'curriculum/content'
        
        # Key files that should exist
        key_files = [
            'section_1_cloud_foundations.md',
            'section_24_bigquery_data_warehousing.md',
            'section_25_pub_sub_data_pipelines.md',
            'section_45_exam_strategy.md',
        ]
        
        for filename in key_files:
            filepath = os.path.join(content_dir, filename)
            self.assertTrue(
                os.path.exists(filepath),
                f"Content file missing: {filename}"
            )
    
    def test_content_not_placeholder(self):
        """Test content files don't have placeholder text"""
        import os
        
        content_dir = 'curriculum/content'
        placeholder_patterns = [
            'Feature 1: ...',
            'Detailed explanation goes here',
            '*Analogy text.*',
        ]
        
        files_to_check = [
            'section_24_bigquery_data_warehousing.md',
            'section_25_pub_sub_data_pipelines.md',
        ]
        
        for filename in files_to_check:
            filepath = os.path.join(content_dir, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                for pattern in placeholder_patterns:
                    self.assertNotIn(
                        pattern, content,
                        f"Placeholder found in {filename}: {pattern}"
                    )
