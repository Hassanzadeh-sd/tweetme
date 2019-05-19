from django.shortcuts import render, HttpResponse
from django.views import View
from .models import HashTag

class tags_view(View):
    def get(self, request, tag, *args, **kwargs):
        tag_obj, created = HashTag.objects.get_or_create(tag=tag)
        return render(request,'hashtags/tag_view.html',{'obj':tag_obj})