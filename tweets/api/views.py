from rest_framework import generics
from .serializers import TweetModelSerializer
from ..models import Tweet
from django.db.models import Q

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                Q(content__contains=query) |
                Q(user__username__contains=query)
            )
        return qs