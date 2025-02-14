from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class Post(models.Model):
    title = models.CharField(default='',max_length=20)
    text = models.TextField(default='',max_length=600)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(default='',max_length=600)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} commented for "{self.post.title}({self.id})" : {self.text}'
    
    def get_absolute_url(self):
        return reverse("blog_list")