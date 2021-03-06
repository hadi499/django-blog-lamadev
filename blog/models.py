from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        default='media/default.jpg', upload_to='media/img')

    def __str__(self):
        return self.title
