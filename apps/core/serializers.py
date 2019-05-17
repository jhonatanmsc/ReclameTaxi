from rest_framework import serializers

from apps.core.models import Reputation, Driver, Platform, ItemPlatform, Report, Comment


class ReputationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reputation
        fields = '__all__'


class PlatformSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Platform


class DriverSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Driver


class ItemPlatformSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ItemPlatform


class ReportSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Report


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment