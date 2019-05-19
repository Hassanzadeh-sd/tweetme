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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_follow"] = UserProfile.objects.is_follow(self.request.user, self.get_object())
        context['recommended'] = UserProfile.objects.recommended(self.request.user)
        return context
    

class toggle_Followview(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User , username = username)

        if request.user.is_authenticated:
            is_follow = UserProfile.objects.toggle_follow(request.user , toggle_user)

        return redirect("profiles:detail", username=username )