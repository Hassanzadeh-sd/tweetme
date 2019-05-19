"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tweets.views import tweet_listview
from hashtags.views import tags_view
from .views import SearchView
from tweets.api.views import SearchTweetAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', tweet_listview.as_view() , name='home'),
    url(r'^search/$', SearchView.as_view() , name='search'),
    url(r'^tweets/', include('tweets.urls', namespace="tweet")),
    url(r'^tags/(?P<tag>.*)/$', tags_view.as_view() , name="hashtag"),
    url(r'^', include('accounts.urls', namespace="profiles")),
    url(r'^api/tweets/', include('tweets.api.urls', namespace="tweet_api")),
    url(r'^api/', include('accounts.api.urls', namespace="profile_api")),
    url(r'^api/search/$', SearchTweetAPIView.as_view() , name='search-api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
