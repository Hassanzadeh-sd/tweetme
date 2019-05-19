import re
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.timesince import timesince
from django.db.models.signals import post_save
from hashtags.signals import parsed_hashtags
from django.utils import timezone
class TweetManager(models.Manager):
    def retweet(self, user , parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        qs = self.get_queryset().filter(user = user,parent = og_parent).filter(
            timestamp__year = timezone.now().year,
            timestamp__month = timezone.now().month,
            timestamp__day = timezone.now().day,
            reply=False,
        )
        if qs.exists():
            return parent_obj

        obj = self.model(
            parent  =  og_parent,
            user    =  user,
            content = parent_obj.content
        )
        obj.save()
        return obj

    def liketoggle(self, user , tweet_obj):
        if (user in tweet_obj.liked.all()):
            is_like = False
            tweet_obj.liked.remove(user)
        else:
            is_like = True
            tweet_obj.liked.add(user)
        
        return is_like

class Tweet(models.Model):
    parent      = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    content     = models.TextField(max_length=140)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    objects     = TweetManager()
    liked       = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True ,related_name='liked')
    reply       = models.BooleanField(verbose_name='is a reply?', default=False)
    
    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk": self.pk})
   
    class Meta:
        ordering = ['-timestamp','content']

    def __str__(self):
        return self.content

    def get_date_display(self):
        return self.timestamp.strftime("%b %d, %Y | at %I:%M %p")

    def get_timesince(self):
        return timesince(self.timestamp) + " ago"        

    def get_parent(self):
        the_parent = self
        if self.parent:
            the_parent = self.parent
        return the_parent

    def get_children(self):
        parent = self.get_parent()
        qs = Tweet.objects.filter(parent=parent)
        qs_parent = Tweet.objects.filter(pk = parent.pk)
        return (qs | qs_parent)    

def post_save_tweet_receiver(sender , instance, created , *args, **kwargs):
    if created:
        user_regx = r'@(?P<username>[\w.@+-]+)'
        usernames = re.findall(user_regx, instance.content)
        print(usernames)

        hashtag_regx = r'#(?P<hashtag>[\w\d-]+)'
        hashtags = re.findall(hashtag_regx ,instance.content)
        parsed_hashtags.send(sender = instance.__class__ ,hashtag_list=hashtags)

post_save.connect(post_save_tweet_receiver, sender=Tweet)