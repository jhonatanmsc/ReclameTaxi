from rest_framework import serializers

from apps.core.models import Reputation, Driver, Platform, ItemPlatform, Report, Comment


class ReputationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reputation
        fields = '__all__'


class PlatformSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Platform
        fields = '__all__'


class DriverSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'


class ItemPlatformSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ItemPlatform
        fields = '__all__'


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    name_driver = serializers.CharField(max_length=90, required=False)
    placa = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = Report
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
