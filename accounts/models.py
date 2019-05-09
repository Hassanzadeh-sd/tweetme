from django.db import models
from django.contrib.auth.models import User

class UserProfileManager(models.Manager):
    def all(self):
        qs = self.get_queryset().all()
        try :
            if(self.instance):
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs
    
    def toggle_follow(self, user , toggle_user):
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if (toggle_user in user_profile.following.all()):
            user_profile.following.remove(toggle_user)
            add = False
        else:
            user_profile.following.add(toggle_user)
            add = True

        return add

    # check if user is not exist in user profile model return false 
    # if exist and follow user return true 
    def is_follow(self, user , followed_by_user):
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            return False
        if (followed_by_user in user_profile.following.all()): 
            return True
        return False 

class UserProfile(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile", blank=True)
    following   = models.ManyToManyField(User,related_name="followed_by", blank=True)   
    objects = UserProfileManager()

    def __str__(self):
        return self.user.username