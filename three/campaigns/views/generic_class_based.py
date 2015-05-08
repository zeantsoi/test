from django.contrib.auth.models import User

from rest_framework import generics

from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer, UserSerializer


class CampaignList(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def pre_save(self, obj):
        obj.user = self.request.user


class CampaignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def pre_save(self, obj):
        obj.user = self.request.user


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer