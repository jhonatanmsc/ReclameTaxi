import pdb

from django.db.models import Q
from rest_framework import serializers

from apps.core.models import Driver, Platform, ItemPlatform, Report, Comment


class PlatformSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Platform
        fields = '__all__'


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    apps = serializers.SerializerMethodField()
    reports = serializers.SerializerMethodField()
    reputation = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = '__all__'

    def get_apps(self, instance):
        # pdb.set_trace()
        item_apps = instance.apps.all()
        apps = []
        for app in item_apps:
            serialized = PlatformSerializer(app.platform, context={'request': self.context['request']})
            apps.append(serialized.data)
        return apps

    def get_reports(self, instance):
        return len(instance.reports.all())

    def get_reputation(self, instace):
        qtd_reports = Report.objects.count()
        if qtd_reports > 0:
            reclamations = Report.objects.filter(Q(resolved=True) & Q(driver=instace)).count()
            if not reclamations:
                return 0
            score = reclamations / qtd_reports
            return score

        return 1


class ItemPlatformSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ItemPlatform
        fields = '__all__'


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    name_driver = serializers.CharField(max_length=90, required=False)
    placa = serializers.CharField(max_length=10, required=False)
    app = serializers.CharField(max_length=20, required=False)
    driver = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = '__all__'

    def get_driver(self, instance):
        item_apps = instance.driver.apps.all()
        apps = []
        for app in item_apps:
            serialized = PlatformSerializer(app.platform, context={'request': self.context['request']})
            apps.append(serialized.data)
        dump_driver = {
            "name": instance.driver.name,
            "placa": instance.driver.placa,
            "apps": apps
        }
        return dump_driver


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
