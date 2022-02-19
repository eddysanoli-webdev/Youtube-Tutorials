from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    # NOTE: on_delete = models.CASCATE == Delete all the posts of a user if the user is deleted
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    # Dunder function (double under)
    # (When a post object is converted to a string, it prints the post title)
    def __str__(self):
        return self.title
