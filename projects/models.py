from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    url = models.URLField(max_length=250, null=True)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.image.path)

        if image.width > 350 or image.height > 350:
            memory_size = (350, 350)
            image.thumbnail(memory_size)
            image.save(self.image.path)

    def get_absolute_url(self):
        return reverse('home')


# Review Model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField()
    design_rate = models.IntegerField(default=0)
    usability_rate = models.IntegerField(default=0)
    content_rate = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)