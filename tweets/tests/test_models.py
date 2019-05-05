from django.test import TestCase
from ..models import Tweet
from django.contrib.auth.models import User
from django.urls import reverse

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_test = User.objects.create_user(username="model_test")
        Tweet.objects.create(user=user_test,content="PROC test content")

    def test_get_absolute_url(self):
        obj = Tweet.objects.first()
        absoulute_url = reverse('tweet:detail', kwargs={'pk':obj.id})
        self.assertEqual(absoulute_url, obj.get_absolute_url())

    def test_golabi(self):
        self.assertEqual(2,2)