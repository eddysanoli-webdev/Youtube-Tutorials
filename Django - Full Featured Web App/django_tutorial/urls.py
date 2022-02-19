"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Rename the import because each app has a views.py module
from users import views as user_views

# Import the default login view
from django.contrib.auth import views as auth_views

# Imports for static files
from django.conf.urls.static import static
from django.conf import settings

# Include the URL files for all apps here
urlpatterns = [

    # Admin page
    path('admin/', admin.site.urls),

    # Register page
    path('register/', user_views.register, name='register'),

    # Login page
    # Use default django login (Class based views)
    #   - template_name: Name of the template to render when using the login page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # Logout page
    # Use default django logout (Class based views)
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # User Profile
    path('profile/', user_views.profile, name='profile'),

    # Root route: Hand that responsibility to the URLS.py file on the blog app
    path('', include('blog.urls'))

] 

# Route for static files (Images)
# Add static file path for debug mode
# (Not suitable for production as files should not be stored locally)
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)