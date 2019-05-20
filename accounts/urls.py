from django.conf.urls import url,include
from .views import (
    account_Detailview,
    toggle_Followview
)

app_name = 'accounts'

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', account_Detailview.as_view(), name='detail'),
    url(r'^(?P<username>[\w-]+)/follow/$', toggle_Followview.as_view(), name='follow'),
] 