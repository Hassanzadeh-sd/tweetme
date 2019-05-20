from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q

def home(request):
    return render(request,'home.html',{})

class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        qs = None
        if query:
            qs= User.objects.filter(Q(username__icontains=query)).exclude(Q(username=request.user))

        context ={'users':qs}
        return render(request, 'search.html' ,context)