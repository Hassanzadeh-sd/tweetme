from django.test import TestCase
from ..views import tweet_listview
from django.contrib.auth.models import User
from ..models import Tweet

class Tweetviewtest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 tweet for pagination tests
        number_of_authors = 13
        test_user = User.objects.create_user("tessssssst")
        for tweet_id in range(number_of_authors):
            Tweet.objects.create(
                user = test_user ,
                content=f'Tweet {tweet_id}',
            )

    def test_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)