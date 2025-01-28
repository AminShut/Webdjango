from django.db import models
from django.conf import settings

class Chatbot(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    messages = models.JSONField(default=list)

    def __str__(self):
        return f"Chatbot by {self.author.username}"