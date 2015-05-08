from django.conf.urls import include, url

from campaigns.views import authenticated

urlpatterns = [
    url(r'^campaigns/$', authenticated.CampaignList.as_view()),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', authenticated.CampaignDetail.as_view()),
]
