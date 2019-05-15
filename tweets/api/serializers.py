from rest_framework import serializers
from ..models import Tweet
from accounts.api.serializers import UserModelSerializer
from django.utils.timesince import timesince

class ParentTweetModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
        ]

    def get_date_display(self , obj):
        return obj.timestamp.strftime("%b %d, %Y | at %I:%M %p")

    def get_timesince(self , obj):
        return timesince(obj.timestamp) + " ago"

class TweetModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    is_retweet = serializers.SerializerMethodField()
    parent = ParentTweetModelSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    didlike = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'is_retweet',
            'parent',
            'likes',
            'didlike'
        ]

    def get_likes(self ,obj):
        return obj.liked.all().count()

    def get_didlike(self,obj):
        user = self.context.get('request').user
        if user in obj.liked.all():
            return True
        return False


    def get_date_display(self , obj):
        return obj.timestamp.strftime("%b %d, %Y | at %I:%M %p")

    def get_timesince(self , obj):
        return timesince(obj.timestamp) + " ago"

    def get_is_retweet(self , obj):
        if obj.parent:
            return True
        return False
