from django.conf.urls import url
from .views import shoppers_list, shopper_detail, predict

urlpatterns = [
    url(r'^predict/$', predict),
    url(r'^shoppers/$', shoppers_list),
    url(r'^shopper/(?P<pk>[0-9]+)/$', shopper_detail),
]
