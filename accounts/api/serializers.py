from rest_framework import serializers
from django.contrib.auth.models import User
from django.urls import reverse

class UserModelSerializer(serializers.ModelSerializer):
    profile_url = serializers.SerializerMethodField()
    follower_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'follower_count',
            'profile_url',
        ]
    
    def get_follower_count(self , obj):
        return 0

    def get_profile_url(self , obj):
        return reverse('profiles:detail',kwargs={'username': obj.username})