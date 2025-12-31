from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('curriculum/', include('curriculum.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')), # Keep this for login/logout
]
