from django.contrib import admin
from .models import Tweet
from .forms import Tweetmodelform

class TweetModelAdmin(admin.ModelAdmin):
    model = Tweet

admin.site.register(Tweet, TweetModelAdmin)