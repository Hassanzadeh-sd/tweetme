from rest_framework import generics
from .serializers import TweetModelSerializer
from ..models import Tweet
from django.db.models import Q
from rest_framework import permissions
from .pagination import TweetsSetPagination
from rest_framework.views import APIView
from rest_framework.response import Response

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = TweetsSetPagination
    
    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get('username')
        if (requested_user):
            qs = Tweet.objects.filter(user__username=requested_user).order_by('-timestamp')
        else:
            im_following = self.request.user.profile.get_following()
            qs1 = Tweet.objects.filter(user__in=im_following).order_by('-timestamp')
            qs2 = Tweet.objects.filter(user=self.request.user)
            qs = (qs1 | qs2)

        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                Q(content__contains=query) |
                Q(user__username__contains=query)
            )
        return qs

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer        
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self ,serializer):
        serializer.save(user=self.request.user)

class RetweetAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = "Not allowed"
 
        if (tweet_qs.exists() and tweet_qs.count() == 1):
            new_tweet = Tweet.objects.retweet(request.user, tweet_qs.first())
            print(new_tweet)
            if (new_tweet != tweet_qs.first()):
                data = TweetModelSerializer(new_tweet).data
                return Response(data)
            message = "Cannot Retweet the same on day"
        return Response({"message": message}, status=400)

class LikeAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = "Not allowed"
        
        if (tweet_qs.exists() and tweet_qs.count() == 1):
            is_like = Tweet.objects.liketoggle(request.user,tweet_qs.first())
            return Response({'liked':is_like})

        return Response({"message": message}, status=400)        