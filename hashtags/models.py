from django.db import models
from django.urls import reverse
from tweets.models import Tweet
from .signals import parsed_hashtags
class HashTag(models.Model):
    tag        = models.CharField(max_length=120)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("hashtag", kwargs={"tag": self.tag})

    def tag_tweets(self):
        return Tweet.objects.filter(content__icontains='#'+self.tag) 

def parsed_hashtag_receiver(sender , hashtag_list , *args, **kwargs):
    for tag in hashtag_list:
        obj,created = HashTag.objects.get_or_create(tag=tag)

parsed_hashtags.connect(parsed_hashtag_receiver)