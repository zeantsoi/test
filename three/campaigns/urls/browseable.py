from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from campaigns.views import browseable

urlpatterns = [
    url(r'^campaigns/$', browseable.campaign_list),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', browseable.campaign_detail),
]
print 'One more small change'
urlpatterns = format_suffix_patterns(urlpatterns)