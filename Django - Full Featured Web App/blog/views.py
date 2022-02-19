from django.shortcuts import render

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

# =====================
# ABOUT PAGE
# =====================

def about(request): 
    return render(request, 'blog/about.html', context = {
        'title': "About"
    })