from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# reverse: Return a string with the URL where the user should be redirected.
# If used inside a class based view, the class will handle the redirect.
from django.urls import reverse

# Each class will be a table in the database
# Each attribute in the post will be a field (column) in the database
class Post(models.Model):

    # A max of 100 characters
    title = models.CharField(max_length=100)

    # Unrestricted text
    content = models.TextField()

    # Set the date to the date when the post was created (default = timezone.now)
    # (You can also use a datetime field with field "auto_now_add" to True. This will
    # set the date at the time of creation of a post. However, this prevents the user
    # from then modifying the date)
    date_posted = models.DateTimeField(default = timezone.now)

    # One to many relationship (One user can have multiple posts)
    # NOTE: on_delete = models.CASCADE == Delete all the posts of a user if the user is deleted
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    # Dunder function (double under)
    # (When a post object is converted to a string, it prints the post title)
    def __str__(self):
        return self.title

    # Where a user should be redirected after a post
    # In this case it will be redirected to the post-detail page. That template requires
    # the ID of the post to be passed, so we pass it through the kwargs. 
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
