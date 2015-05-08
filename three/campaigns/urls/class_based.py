from django.conf.urls import include, url

from campaigns.views import class_based

urlpatterns = [
    url(r'^campaigns/$', class_based.CampaignList.as_view()),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', class_based.CampaignDetail.as_view()),
]
