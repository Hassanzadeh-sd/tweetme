from .models import Tweet
from django import forms

class Tweetmodelform(forms.ModelForm):
    class meta:
        model = Tweet
        fields = [
            'user',
        ]