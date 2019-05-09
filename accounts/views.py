from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.urls import reverse
from django.views import View
from .models import UserProfile

class account_Detailview(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'obj_user'
    template_name = 'accounts/profiles.html'

class toggle_Followview(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User , username = username)
        
        try:
            if request.user.is_authenticated():
                user_profile, created = UserProfile.objects.get_or_create(user=request.user)
                if (toggle_user in user_profile.following.all()):
                    user_profile.following.remove(toggle_user)
                else:
                    user_profile.following.add(toggle_user)
        except:
            pass

        return redirect("profiles:detail", username=username )