from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import reverse
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

    def is_follow(self, user , followed_by_user):
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            return False
        if (followed_by_user in user_profile.following.all()): 
            return True
        return False 

    def recommended(self, user, limit_to=10):
        profile = user.profile
        following = profile.following.all()
        qs = self.get_queryset().exclude(user__in=following).exclude(id=profile.id).order_by("?")[:limit_to]
        return qs
class UserProfile(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile", blank=True)
    following   = models.ManyToManyField(User,related_name="followed_by", blank=True)   
    objects = UserProfileManager()
    avatar      = models.ImageField(upload_to='images/', default = '/images/NoProfile.jpg', null=True, blank=True )

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)
    
    def get_follow_url(self):
        return reverse('profiles:follow', username=self.user.username)

    def __str__(self):
        return self.user.username


def post_save_user_receiver(sender , instance, created , *args, **kwargs):
    print("HIIII SIGNAL")
    print(instance)
    if created:
        try:
            new_profile = UserProfile.objects.get_or_created(user = instance)
        except:
            pass


post_save.connect(post_save_user_receiver, sender=User)