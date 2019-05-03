from django.shortcuts import render
from .models import Tweet
from django.views.generic import DetailView, ListView, CreateView
from django.db.models import Q
from .forms import Tweetmodelform
from django.urls import reverse
class tweet_listview(ListView):
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
    
class tweet_Detailview(DetailView):
    template_name = 'tweets/detail_view.html'
    def get_object(self):
        print (self.kwargs)
        print(self.kwargs['pk'])
        id=self.kwargs.get('pk')
        return Tweet.objects.get(id=id)

class tweet_Createview(CreateView):
    form_class = Tweetmodelform
    template_name = 'tweets/create_view.html'

    def form_valid(self , form):
        form.instance.user = self.request.user
        return super(tweet_Createview, self).form_valid(form)















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