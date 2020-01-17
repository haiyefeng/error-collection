# _*_ coding: utf-8 _*_
__author__ = 'fortune'
__date__ = '2019/12/26 10:19'
from rest_framework import routers as drf_routers
from miscollection.views import MistakeViewSet, SummaryViewSet

routers = drf_routers.DefaultRouter(trailing_slash=True)

routers.register('mistakes', MistakeViewSet, basename='mistakes')
routers.register('summary', SummaryViewSet, basename='summary')

urlpatterns = routers.urls
