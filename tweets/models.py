from django.db import models
from django.conf import settings

class Tweet(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    content     = models.TextField(max_length=140)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content