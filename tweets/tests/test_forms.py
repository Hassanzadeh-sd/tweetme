from django.test import TestCase
from ..forms import Tweetmodelform

class TweetmodelformTest(TestCase):
    def test_form_valid(self):
        form = Tweetmodelform(data={'content':'teeeeeest'})
        print("form is valid")
        self.assertTrue(form.is_valid())

        