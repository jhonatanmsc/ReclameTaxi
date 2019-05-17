import pdb

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.core.models import Reputation, Platform, Driver, Report, Comment
from apps.core.serializers import ReputationSerializer, PlatformSerializer, ReportSerializer, CommentSerializer


class ReputationView(viewsets.ModelViewSet):
    queryset = Reputation.objects.all()
    serializer_class = ReputationSerializer
    permission_classes = (IsAuthenticated, )


class PlatformView(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = (IsAuthenticated, )


class DriverView(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = ''
    permission_classes = (IsAuthenticated, )


class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated, )


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
