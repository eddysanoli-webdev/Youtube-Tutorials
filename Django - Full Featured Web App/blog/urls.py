from django.urls import path

# Import views.py file in current directory (.)
from . import views

# TIPS: 
# - Be clear with the naming of the paths. Avoid generic names like "home"
# - Always add a trailing slash to all routes
urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]