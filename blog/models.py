from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class Post(models.Model):
    title = models.CharField(default='',max_length=20)
    text = models.TextField(default='',max_length=600)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.id})
    

