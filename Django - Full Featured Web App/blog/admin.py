from django.contrib import admin

# Import your model
from .models import Post

# Make your model available inside the admin page
admin.site.register(Post)
