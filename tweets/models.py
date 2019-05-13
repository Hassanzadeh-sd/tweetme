from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.timesince import timesince

class TweetManager(models.Manager):
    def retweet(self, user , parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        obj = self.model(
            parent  =  og_parent,
            user    =  user,
            content = parent_obj.content
        )
        obj.save()
        return obj

class Tweet(models.Model):
    parent      = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    content     = models.TextField(max_length=140)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    objects     = TweetManager()

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