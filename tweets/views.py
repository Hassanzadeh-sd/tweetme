from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Tweet
from django.views.generic import DetailView, ListView, CreateView, View
from django.db.models import Q
from .forms import Tweetmodelform
from django.http import HttpResponseRedirect
from django.urls import reverse
class tweet_listview(LoginRequiredMixin ,ListView):
    def get_queryset(self):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                Q(content__contains=query) |
                Q(user__username__contains=query)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = Tweetmodelform()
        context['create_url'] = reverse("tweet:create")
        return context
    
class tweet_Detailview(LoginRequiredMixin,DetailView):
    template_name = 'tweets/detail_view.html'
    def get_object(self):
        print (self.kwargs)
        print(self.kwargs['pk'])
        id=self.kwargs.get('pk')
        return Tweet.objects.get(id=id)

class tweet_Createview(LoginRequiredMixin,CreateView):
    form_class = Tweetmodelform
    template_name = 'tweets/create_view.html'

    def form_valid(self , form):
        form.instance.user = self.request.user
        return super(tweet_Createview, self).form_valid(form)

class retweet_View(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk = pk)
        if request.user.is_authenticated:
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect(new_tweet.get_absolute_url())
        return  HttpResponseRedirect(tweet.get_absolute_url())








# def tweet_detail_view(request, id):
#     obj = Tweet.objects.get(pk=id)
#     context = {
#         'object' : obj
#     }
#     return render(request, 'tweets/detail_view.html', context)

# def tweet_list_view(request):
#     query_set = Tweet.objects.all()
#     context = {
#         'object_list':query_set
#     }
#     return render(request, 'tweets/list_view.html', context)