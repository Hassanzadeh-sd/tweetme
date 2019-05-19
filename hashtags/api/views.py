from rest_framework import generics
from tweets.api.serializers import TweetModelSerializer
from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions
from tweets.api.pagination import TweetsSetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from hashtags.models import HashTag

class TagTweetAPIView(generics.ListAPIView):
    queryset = Tweet.objects.all().order_by("-timestamp")
    serializer_class = TweetModelSerializer
    pagination_class = TweetsSetPagination

    def get_queryset(self, *args, **kwargs):
        hashtag = self.kwargs.get('tag')
        hashtag_obj = None

        try :
            hashtag_obj = HashTag.objects.get_or_create(tag=hashtag)[0]
        except:
            pass

        if (hashtag_obj):
            qs = hashtag_obj.tag_tweets()
            query = self.request.GET.get("q",None)
            if query is not None:
                qs = qs.filter(
                    Q(content__contains=query) |
                    Q(user__username__contains=query)
                )
            return qs
        return None


    def get_serializer_context(self , *args, **kwargs):
        context = super(TagTweetAPIView, self).get_serializer_context()
        context['request'] = self.request
        return context