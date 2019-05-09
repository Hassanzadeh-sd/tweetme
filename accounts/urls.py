from django.conf.urls import url
from .views import (
    account_Detailview,
)

app_name = 'accounts'

urlpatterns = [
    # url(r'^search/$', tweet_listview.as_view(), name='search'),
    # url(r'^create/$', tweet_Createview.as_view(), name='create'),
    url(r'^(?P<username>[\w-]+)/$', account_Detailview.as_view(), name='detail'),
] 