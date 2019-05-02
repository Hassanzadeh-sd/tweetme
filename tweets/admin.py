from django.contrib import admin
from .models import Tweet
from .forms import Tweetmodelform

class TweetModelAdmin(admin.ModelAdmin):
    form = Tweetmodelform

admin.site.register(Tweet, TweetModelAdmin)