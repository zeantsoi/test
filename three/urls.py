from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.models import User


urlpatterns = patterns('',
    url(r'^basic/', include('campaigns.urls.basic')),
    url(r'^browseable/', include('campaigns.urls.browseable')),
    url(r'^class_based/', include('campaigns.urls.class_based')),
    url(r'^generic_class_based/', include('campaigns.urls.generic_class_based')),
    url(r'^authenticated/', include('campaigns.urls.authenticated')),
    url(r'^viewset/', include('campaigns.urls.viewset')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
