from django.db import models
from django.contrib.auth.models import User

class UserProfileManager(models.Manager):
    def all(self):
        qs = self.get_queryset().all()
        try :
            if(self.instance):
                qs = qs.exclude(user=self.instance)
                print(qs)
        except:
            pass
        return qs

class UserProfile(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile", blank=True)
    following   = models.ManyToManyField(User,related_name="followed_by", blank=True)   
    objects = UserProfileManager()

    def __str__(self):
        return str(self.following.all().count())