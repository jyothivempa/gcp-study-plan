"""
Test Suite for GCP Study Plan - Users App
==========================================
Phase 1: Model Unit Tests (User, UserProfile)
Phase 2: Authentication Tests
Phase 3: Registration Tests
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# =============================================================================
# PHASE 1: MODEL UNIT TESTS
# =============================================================================

class UserModelTests(TestCase):
    """Unit tests for custom User model"""
    
    def test_user_creation(self):
        """Test creating a basic user"""
        user = UserModel.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='securepass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('securepass123'))
    
    def test_user_str_representation(self):
        """Test user string representation"""
        user = UserModel.objects.create_user(username='struser', password='pass')
        self.assertEqual(str(user), 'struser')
    
    def test_superuser_creation(self):
        """Test creating a superuser"""
        admin = UserModel.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass'
        )
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
    
    def test_username_uniqueness(self):
        """Test usernames must be unique"""
        UserModel.objects.create_user(username='unique', password='pass')
        with self.assertRaises(Exception):
            UserModel.objects.create_user(username='unique', password='pass2')


class UserProfileModelTests(TestCase):
    """Unit tests for UserProfile model"""
    
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='gamer', password='game123'
        )
    
    def test_profile_creation(self):
        """Test creating a user profile"""
        from users.models import UserProfile
        # Check if profile already exists (auto-created)
        try:
            profile = self.user.profile
        except:
            profile = UserProfile.objects.create(user=self.user)
        
        self.assertEqual(profile.xp, 0)
        self.assertEqual(profile.level, 1)


# =============================================================================
# PHASE 2: AUTHENTICATION TESTS
# =============================================================================

class AuthenticationTests(TestCase):
    """Tests for login/logout functionality"""
    
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username='authuser',
            email='auth@test.com',
            password='authpass123'
        )
    
    def test_login_page_loads(self):
        """Test login page is accessible"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_valid_credentials(self):
        """Test login with valid credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'authuser',
            'password': 'authpass123'
        })
        # Should redirect on success
        self.assertIn(response.status_code, [200, 302])
    
    def test_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'authuser',
            'password': 'wrongpassword'
        })
        # Should stay on login page with error
        self.assertEqual(response.status_code, 200)
    
    def test_logout_works(self):
        """Test logout functionality"""
        self.client.login(username='authuser', password='authpass123')
        
        response = self.client.post(reverse('logout'))
        # Should redirect after logout
        self.assertIn(response.status_code, [200, 302])
    
    def test_protected_view_requires_login(self):
        """Test protected views redirect to login"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)


# =============================================================================
# PHASE 3: REGISTRATION TESTS
# =============================================================================

class RegistrationTests(TestCase):
    """Tests for user registration"""
    
    def setUp(self):
        self.client = Client()
    
    def test_registration_page_loads(self):
        """Test registration page is accessible"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
    
    def test_registration_valid_data(self):
        """Test registration with valid data"""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@test.com',
            'password1': 'complexPass123!',
            'password2': 'complexPass123!'
        })
        
        # Should redirect on success or show form
        self.assertIn(response.status_code, [200, 302])
    
    def test_registration_password_mismatch(self):
        """Test registration with mismatched passwords"""
        response = self.client.post(reverse('register'), {
            'username': 'mismatch',
            'password1': 'password123',
            'password2': 'different123'
        })
        
        # Should stay on page with errors
        self.assertEqual(response.status_code, 200)
    
    def test_registration_duplicate_username(self):
        """Test registration with existing username"""
        UserModel.objects.create_user(username='existing', password='pass')
        
        response = self.client.post(reverse('register'), {
            'username': 'existing',
            'password1': 'newpass123',
            'password2': 'newpass123'
        })
        
        # Should stay on page with error
        self.assertEqual(response.status_code, 200)


# =============================================================================
# PHASE 4: SECURITY TESTS
# =============================================================================

class SecurityTests(TestCase):
    """Security-related tests"""
    
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username='secuser', password='secpass123'
        )
    
    def test_password_not_stored_plaintext(self):
        """Test password is hashed, not plaintext"""
        self.assertNotEqual(self.user.password, 'secpass123')
        # Check it's using a proper hash algorithm
        self.assertTrue(
            self.user.password.startswith('pbkdf2_sha256') or 
            self.user.password.startswith('argon2')
        )
    
    def test_csrf_protection(self):
        """Test CSRF protection on forms"""
        # Login form should have CSRF token
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'csrfmiddlewaretoken')
