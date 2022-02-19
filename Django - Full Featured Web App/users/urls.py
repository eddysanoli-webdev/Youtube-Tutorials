from django.urls import path

# Import views.py file in current directory (.)
from . import views

# TIPS: 
# - Be clear with the naming of the paths. Avoid generic names like "home"
# - Always add a trailing slash to all routes
urlpatterns = [
    path('register/', views.register, name="users-register")
]