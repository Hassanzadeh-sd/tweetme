from django.shortcuts import render, HttpResponse
from django.views import View
from .models import HashTag

class tags_view(View):
    def get(self, request, tag, *args, **kwargs):
        tag_tweets, created = HashTag.objects.get_or_create(tag=tag)
        return render(request,'hashtags/tag_view.html',{'tag_tweets':tag_tweets.tag_tweets})