from django.contrib import admin

# Import Profile model
from .models import Profile

# Make your model available inside the admin page
admin.site.register(Profile)
