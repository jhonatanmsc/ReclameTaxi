import pdb

from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.core.models import Reputation, Platform, Driver, Report, Comment, ItemPlatform
from apps.core.serializers import ReputationSerializer, PlatformSerializer, ReportSerializer, CommentSerializer, \
    DriverSerializer, ItemPlatformSerializer


class ReputationView(viewsets.ModelViewSet):
    queryset = Reputation.objects.all()
    serializer_class = ReputationSerializer


class PlatformView(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class ItemPlatformView(viewsets.ModelViewSet):
    queryset = ItemPlatform.objects.all()
    serializer_class = ItemPlatformSerializer


class DriverView(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def create(self, request):
        uid = None if not request.user else request.user.uid
        driver, created = Driver.objects.get_or_create(
            name=request.data['name_driver'].upper(), placa=request.data['placa'].upper()
        )

        report = Report.objects.create(uid=uid, descr=request.data['descr'], driver=driver)

        headers = self.get_success_headers(request.data)
        return Response({'Message': 'Reclamação registrada.'}, status=status.HTTP_201_CREATED, headers=headers)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
        responseJSON = request.data['body']
        uid = None if not request.user else request.user.uid
        report = Report.objects.get(id=responseJSON['reportId'])

        comment = Comment.objects.create(uid=uid, descr=responseJSON['descr'], report=report)

        headers = self.get_success_headers(request.data)
        return Response({'Message': 'Comentário registrado.'}, status=status.HTTP_201_CREATED, headers=headers)
