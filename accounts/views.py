from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.urls import reverse


class account_Detailview(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'obj_user'
    template_name = 'accounts/profiles.html'