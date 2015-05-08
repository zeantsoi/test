from django.contrib.auth.models import User
from django.forms import widgets
from rest_framework import serializers

from campaigns.models import Campaign, CAMPAIGN_TYPES


class CampaignSerializer(serializers.Serializer):
    pk = serializers.Field()
    name = serializers.CharField()
    slug = serializers.CharField()
    campaign_type = serializers.ChoiceField(choices=CAMPAIGN_TYPE, default=CAMPAIGN_TYPE[0])
    # user = serializers.Field(source='user.username')

    def create(self, validated_data):
        """
        Create and return a new `Campaign` instances comprised of the validated data.
        """
        return Campaign.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Campaign` instance
        based on the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.ended_at = validated_data.get('name', instance.slug)
        instance.save()
        return instance

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.slug = attrs.get('slug', instance.slug)
            instance.ended_at = attrs.get('ended_at', instance.ended_at)
            return instance

        # Create new instance
        return Campaign(**attrs)


class UserSerializer(serializers.ModelSerializer):
    campaigns = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'campaigns')