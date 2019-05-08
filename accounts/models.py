from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile", blank=True)
    following   = models.ManyToManyField(User,related_name="followed_by", blank=True)   

    def __str__(self):
        return str(self.following.all().count())