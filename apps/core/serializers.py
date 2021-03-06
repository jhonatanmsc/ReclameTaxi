import pdb

from django.db.models import Q
from rest_framework import serializers

from apps.core.models import Driver, Platform, ItemPlatform, Report, Comment


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    reputation = serializers.SerializerMethodField()

    class Meta:
        model = Platform
        fields = '__all__'

    def get_reputation(self, instace):
        qtd_reports = Report.objects.filter(Q(driver__apps__platform__name=instace.name)).count()
        if qtd_reports > 0:
            reclamations = Report.objects.filter(
                Q(resolved=True) &
                Q(driver__apps__platform__name=instace.name))\
                .count()
            if not reclamations:
                return 0
            score = qtd_reports / reclamations
            return score

        return 1


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
            score = qtd_reports / reclamations
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
    driver = DriverSerializer()

    class Meta:
        model = Report
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
