from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Model for the user profile info
# (Must have a one to one relationship with the User model)
class Profile(models.Model):

    # Generate a one to one relationship with the User model
    #   - on_delete: If the user is deleted, the profile is also deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Image field for the profile picture
    #   - default: Default image if no image exists (Add the image inside the MEDIA_ROOT directory)
    #   - upload_to: Directory in which the new image will be saved
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # Default name of profile object: Username
    def __str__(self):
        return f'{self.user.username} Profile'

    # Overwrite default save method from parent class
    def save(self):

        # Execute the "save" method of the parent class
        super().save()

        # Open image of the current instance
        img = Image.open(self.image.path)

        # Resize image if a dimension is larger than 300
        if img.height > 300 or img.width > 300:

            # Creates a scaled down version of the image that retains its proportions
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

