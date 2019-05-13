from .models import Tweet
from django import forms

class Tweetmodelform(forms.ModelForm):
    content = forms.CharField(label='', 
                    widget=forms.Textarea(
                            attrs={'placeholder':'your message',
                                    'class':'form-control'}
                            ))
    class Meta:
        model = Tweet
        fields = [
            'parent',
            'content'
        ]