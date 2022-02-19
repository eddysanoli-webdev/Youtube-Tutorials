from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# From the "models.py" file on the current directory
from .models import Post

# =====================
# HOME PAGE
# =====================
# Handle the traffic from our home page
# Return what we want the user to see

def home(request):

    # NOTE: "render" still returns an HTTP response under the hood
    return render(request, 'blog/home.html', context = {
        'posts': Post.objects.all()
    })

# Class List View
class PostListView(ListView):

    # Model to query to list the elements
    model = Post

    # Set a new template to use the template used on the home function view
    template_name = 'blog/home.html'

    # By default, the element that the template will loop over is called object_list
    # Here we want to loop over our Post objects, so we create a new name for "object_list"
    # element. Since in the "home" template we use "posts" that will be the name
    context_object_name = 'posts'

    # Order posts from latest to oldest
    #   1. Order from oldest to latest: ['date_posted']
    #   2. Reverse the order: ['-date_posted']
    ordering = ['-date_posted']

# =====================
# ABOUT PAGE
# =====================

def about(request): 
    return render(request, 'blog/about.html', context = {
        'title': "About"
    })


# =====================
# POST DETAIL PAGE
# =====================

# Class based view will look for a template called:
#   <app>/<model>_<viewtype>.html = blog/post_detail.html

class PostDetailView(DetailView):
    model = Post


# =====================
# POST CREATE PAGE
# =====================

# Class based view will look for a template called:
#   <app>/<model>_<viewtype>.html = blog/post_create.html

# We cannot use decorators on classes, so the "login_required" decorator cannot
# be used to require a login. In this case we inherit from the "LoginRequired" mixin.

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    # Fields that we want to be in the Create form
    fields = ['title', 'content']

    # Overwrite the "form_valid" method from the parent to add a user
    # to the post, preventing an error
    def form_valid(self, form):

        # Set the author of the form as the currently logged in user
        form.instance.author = self.request.user

        # Running the "form_valid" method from the parent class
        return super().form_valid(form)

# =====================
# POST UPDATE PAGE
# =====================

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Post

    # Fields that we want to be in the Create form
    fields = ['title', 'content']


    # Overwrite the "form_valid" method from the parent to add a user
    # to the post, preventing an error
    def form_valid(self, form):

        # Set the author of the form as the currently logged in user
        form.instance.author = self.request.user

        # Running the "form_valid" method from the parent class
        return super().form_valid(form)


    # Function that the UserPassesTestMixin will use to check if a user
    # passes a specific test or condition
    def test_func(self):

        # Get the current post
        post = self.get_object()

        # If current user == current post author then
        # allow the user to edit the post
        if self.request.user == post.author:
            return True
        else:
            return False


# =====================
# POST DELETE PAGE
# =====================

# To delete a view, the user must be logged in and be the author of the post

# Class based view will look for a template called:
#   <app>/<model>_<viewtype>.html = blog/post_confirm_delete.html

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    # Redirect to the home page after a successful deletion
    success_url = "/"

    # Check if the user is the author of the current post
    def test_func(self):

        # Get the current post
        post = self.get_object()

        # If current user == current post author
        if self.request.user == post.author:
            return True
        else:
            return False