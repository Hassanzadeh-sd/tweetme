from rest_framework import generics
from .serializers import TweetModelSerializer
from ..models import Tweet

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    queryset = Tweet.objects.all()
    