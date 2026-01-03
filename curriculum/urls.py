from django.urls import path
from . import views

urlpatterns = [
    path('', views.curriculum_overview, name='curriculum_overview'),
    path('course/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('course/<slug:course_slug>/day/<int:day_number>/', views.lesson_detail, name='lesson_detail'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('certificate/', views.certificate_view, name='certificate'),
    path('ace-guide/', views.ace_guide, name='ace_guide'),
    path('style-guide/', views.style_guide, name='style_guide'),
    path('ace-cheat-sheet/', views.ace_cheat_sheet, name='ace_cheat_sheet'),
    
    path('api/ask_ai/', views.ask_ai, name='ask_ai'),
    path('api/save_note/<int:day_number>/', views.save_note, name='save_note'),
    path('search/', views.search_lessons, name='search_lessons'),
    path('api/verify_capstone/', views.verify_capstone, name='verify_capstone'),
    path('api/sidebar_data/<slug:course_slug>/<int:day_number>/', views.get_sidebar_data, name='get_sidebar_data'),
    path('faq/', views.faq, name='faq'),
]
