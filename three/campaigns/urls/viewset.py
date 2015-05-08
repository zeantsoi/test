from django.conf.urls import include, url

from campaigns.views import viewset

campaign_list = viewset.CampaignViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

campaign_detail = viewset.CampaignViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

user_list = viewset.UserViewSet.as_view({
    'get': 'list'
})
user_detail = viewset.UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^campaigns/$', campaign_list),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', campaign_detail),
    url(r'^users/$', user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail),
]

# urlpatterns = format_suffix_patterns(urlpatterns)