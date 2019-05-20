from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.urls import reverse
from django.views import View
from .models import UserProfile
from django.views.generic.edit import FormView
from .forms import RegisterForm


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = "/login/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password1)
        new_user.save()
        print("FORMVALID")
        return super(RegisterView, self).form_valid(form)

class account_Detailview(LoginRequiredMixin,DetailView):
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