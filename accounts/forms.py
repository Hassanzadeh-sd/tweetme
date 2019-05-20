from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username    = forms.CharField()
    email       = forms.EmailField()
    password1   = forms.CharField(widget=forms.PasswordInput,label="Password")
    password2   = forms.CharField(widget=forms.PasswordInput,label="Confirm password")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("The username is token")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if  (password1 != password2):
            raise forms.ValidationError("password confirm not same")
        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("The email is already registered")
        return email