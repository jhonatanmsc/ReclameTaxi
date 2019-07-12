import pdb, sys

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.core.models import Platform, Driver, Report, Comment, ItemPlatform
from apps.core.serializers import PlatformSerializer, ReportSerializer, CommentSerializer, \
    DriverSerializer, ItemPlatformSerializer


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

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        uid = request.query_params.get('uid')

        if uid:
            report_list = Report.objects.filter(uid=uid)
        else:
            report_list = self.queryset

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(report_list, many=True)
        return Response(serializer.data)

    def create(self, request):
        uid = request.data['uid'] if request.user.is_anonymous else request.user.uid
        try:
            app = Platform.objects.get(name=request.data['app'].upper())
            driver, driver_created = Driver.objects.get_or_create(
                name=request.data['name_driver'].upper(),
                placa=request.data['placa'].upper(),
            )
            item, item_created = ItemPlatform.objects.get_or_create(
                platform=app,
                driver=driver
            )
            report = Report.objects.create(uid=uid, descr=request.data['descr'], driver=driver)
            headers = self.get_success_headers(request.data)
            return Response(
                {'Message': 'Reclamação registrada.'},
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        except ObjectDoesNotExist:
            # pdb.set_trace()
            sys.stderr.write(f'App {request.data["app"]} não encontrado\n')
            return Response(
                {'Message': f'App {request.data["app"]} não encontrado'},
                status=status.HTTP_404_NOT_FOUND,
            )


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
        responseJSON = request.data['body']
        uid = request.data['uid'] if not request.user else request.user.uid
        report = Report.objects.get(id=responseJSON['reportId'])

        comment = Comment.objects.create(uid=uid, descr=responseJSON['descr'], report=report)

        headers = self.get_success_headers(request.data)
        return Response({'Message': 'Comentário registrado.'}, status=status.HTTP_201_CREATED, headers=headers)
