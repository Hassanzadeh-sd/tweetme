from rest_framework import generics
from .serializers import TweetModelSerializer
from ..models import Tweet
from django.db.models import Q
from rest_framework import permissions

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all().order_by('-timestamp')
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
