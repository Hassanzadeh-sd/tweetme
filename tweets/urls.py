from django.conf.urls import url
from .views import (
    tweet_Detailview,
    tweet_listview
)

urlpatterns = [
    url(r'^$', tweet_listview.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', tweet_Detailview.as_view(), name='detail'),
] 