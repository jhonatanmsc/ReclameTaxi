"""system URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.core.views import ReportView, CommentView, DriverView, ReputationView, PlatformView
from apps.user.views import UserView

router = routers.DefaultRouter()
router.register(r'reclamacao', ReportView)
router.register(r'motorista', DriverView)
router.register(r'app', PlatformView)
router.register(r'comentario', CommentView)
router.register(r'reputacao', ReputationView)
router.register(u'usuario', UserView)

urlpatterns = router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
