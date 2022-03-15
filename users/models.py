from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_bio = models.TextField()
    user_contact = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.width > 350 or img.height > 350:
            memory_size = (350, 350)
            img.thumbnail(memory_size)
            img.save(self.image.path)
# Create your models here.
