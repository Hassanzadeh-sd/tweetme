from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import (
    retweet_View,
    tweet_Detailview,
    tweet_listview,
    tweet_Createview,
)

app_name = 'tweets'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/'), name='list'),
    url(r'^search/$', tweet_listview.as_view(), name='search'),
    url(r'^create/$', tweet_Createview.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', tweet_Detailview.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/retweet/$', retweet_View.as_view(), name='retweet'),
] 