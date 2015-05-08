from django.contrib.auth.models import User
from django.forms import widgets
from rest_framework import serializers

from campaigns.models import Campaign, CAMPAIGN_TYPES
    
class UserSerializer(serializers.ModelSerializer):
    # Must be explicitly set to `read_only=True`
    campaigns = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'campaigns')


class CampaignSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = Campaign
        fields = ('id', 'user', 'foo', 'bar', 'qux', 'name', 'slug', 'campaign_type')
