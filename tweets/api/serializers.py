from rest_framework import serializers
from ..models import Tweet
from accounts.api.serializers import UserModelSerializer

class TweetModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content'
        ]