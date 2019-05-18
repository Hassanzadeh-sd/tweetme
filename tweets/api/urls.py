from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import (
    LikeAPIView,
    RetweetAPIView,
    TweetListAPIView,
    TweetCreateAPIView,
    TweetDetailAPIView,
)

app_name = "tweets"

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view() , name='list'),
    url(r'^create/$', TweetCreateAPIView.as_view() , name='create'),
    url(r'^retweet/(?P<pk>\d+)/$', RetweetAPIView.as_view(), name='retweet'),
    url(r'^like/(?P<pk>\d+)/$', LikeAPIView.as_view(), name='like'),
    url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name='detail'),
] 