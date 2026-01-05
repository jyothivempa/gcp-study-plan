from django.urls import path, include
from . import views, api

urlpatterns = [
    # Template Views
    path('', views.curriculum_overview, name='curriculum_overview'),
    path('course/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('course/<slug:course_slug>/day/<int:day_number>/', views.lesson_detail, name='lesson_detail'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('certificate/', views.certificate_view, name='certificate'),
    path('ace-guide/', views.ace_guide, name='ace_guide'),
    path('style-guide/', views.style_guide, name='style_guide'),
    path('ace-cheat-sheet/', views.ace_cheat_sheet, name='ace_cheat_sheet'),
    path('search/', views.search_lessons, name='search_lessons'),
    path('faq/', views.faq, name='faq'),
    
    # Legacy/Internal APIs
    path('api/ask_ai/', views.ask_ai, name='ask_ai'),
    path('api/save_note/<int:day_number>/', views.save_note, name='save_note'),
    path('api/verify_capstone/', views.verify_capstone, name='verify_capstone'),
    path('api/sidebar_data/<slug:course_slug>/<int:day_number>/', views.get_sidebar_data, name='get_sidebar_data'),

    # REST API v2 (New)
    path('api/v2/courses/', api.course_list, name='api_course_list'),
    path('api/v2/courses/<slug:course_slug>/', api.course_detail_api, name='api_course_detail'),
    path('api/v2/courses/<slug:course_slug>/days/<int:day_number>/', api.day_detail_api, name='api_day_detail'),
    
    path('api/v2/progress/', api.progress_summary, name='api_progress_summary'),
    path('api/v2/progress/days/', api.progress_list, name='api_progress_list'),
    path('api/v2/progress/<int:day_number>/complete/', api.mark_complete, name='api_mark_complete'),
    path('api/v2/progress/<int:day_number>/incomplete/', api.mark_incomplete, name='api_mark_incomplete'),
    
    path('api/v2/quiz/<int:day_number>/', api.quiz_questions, name='api_quiz_questions'),
    path('api/v2/quiz/<int:day_number>/submit/', api.submit_quiz, name='api_submit_quiz'),
    
    path('api/v2/notes/<int:day_number>/', api.user_note, name='api_user_note'),
    path('api/v2/search/', api.search_api, name='api_search_api'),
]
