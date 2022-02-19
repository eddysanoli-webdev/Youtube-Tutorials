from django.urls import path

# Import views.py file in current directory (.)
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostListView
)

# TIPS: 
# - Be clear with the naming of the paths. Avoid generic names like "home"
# - Always add a trailing slash to all routes
urlpatterns = [
    
    # Home view
    # By default, the list view will look for a template called: APP/MODEL_VIEWTYPE.html
    path('', PostListView.as_view(), name='blog-home'),
    # Function alternative: path('', views.home, name="blog-home")

    # View to any Post
    #   - By default, the class view expects the parameter to be "pk" (primary key). This can be changed by adding an attribute inside the class
    #   - <param>: Parameter received through the URL
    #   - <data_type:...>: Assert a specific type for a URL parameter
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Create post view
    # Note: The post will share a template with the "post-update" view. The template
    #       should be called "post_form.html". Make sure to modify the "form_valid" method
    #       of the class and add the parameter "get_absolute_url" to "models.py"
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Update Post View
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Delete Post View
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Filter Posts by User
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),

    # About view
    path('about/', views.about, name="blog-about"),
]