from django.conf.urls import include, url

from campaigns.views import basic

urlpatterns = [
    url(r'^campaigns/$', basic.campaign_list),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', basic.campaign_detail),

]
