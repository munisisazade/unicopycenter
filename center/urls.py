from django.conf.urls import url
from center.views import IndexRequestView





urlpatterns = [
    url(r'^$', IndexRequestView.as_view(), name='index'),
]