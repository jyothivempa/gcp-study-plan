# 30-Day GCP Daily Study Plan LMS

A Django-based Learning Management System designed to guide beginners from zero to Google Associate Cloud Engineer in 30 days.

## Features
- **30-Day Structured Curriculum**: Day-by-day lesson plan.
- **Progress Tracking**: User accounts to track completed days.
- **Coursera-Style UI**: Clean, focus-oriented interface.
- **Interactive Lessons**: Concepts, Hands-on labs, and Interview questions for each day.

## Tech Stack
- **Backend**: Django 6.0, Django Rest Framework
- **Frontend**: HTML5, Vanilla CSS (Custom Design System)
- **Database**: SQLite (Production-ready for low traffic/learning)

## Setup Instructions

### Prerequisites
- Python 3.10+ installed.

### Installation

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd gcp_study_plan
   ```

2. **Install Dependencies**:
   ```bash
   pip install django djangorestframework
   ```

3. **Initialize Database**:
   ```bash
   python manage.py migrate
   ```

4. **Populate Course Content**:
   Run the custom management command to seed the database with the 30-day curriculum:
   ```bash
   python manage.py populate_content
   ```

5. **Create Superuser** (Optional, for Admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the App**:
   Open browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage
- **Sign Up**: Create a new account.
- **Start Learning**: Go to the Curriculum page and start Day 1.
- **Track Progress**: Click "Mark as Completed" on each lesson to track your journey.

## Contributing
Project designed for educational purposes.
