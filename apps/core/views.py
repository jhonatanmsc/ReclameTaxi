import pdb

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.core.models import Reputation, Platform, Driver, Report, Comment, ItemPlatform
from apps.core.serializers import ReputationSerializer, PlatformSerializer, ReportSerializer, CommentSerializer, \
    DriverSerializer, ItemPlatformSerializer


class ReputationView(viewsets.ModelViewSet):
    queryset = Reputation.objects.all()
    serializer_class = ReputationSerializer
    permission_classes = (IsAuthenticated, )


class PlatformView(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = (IsAuthenticated, )


class ItemPlatformView(viewsets.ModelViewSet):
    queryset = ItemPlatform.objects.all()
    serializer_class = ItemPlatformSerializer
    permission_classes = (IsAuthenticated,)


class DriverView(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (IsAuthenticated, )


class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.queryset

    def create(self, request):
        driver, created = Driver.objects.get_or_create(
            name=request.data['name_driver'].upper(), placa=request.data['placa'].upper()
        )

        report = Report.objects.create(descr=request.data['descr'], driver=driver)

        headers = self.get_success_headers(request.data)
        return Response({'Message': 'Reclamação registrada.'}, status=status.HTTP_201_CREATED, headers=headers)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
