# -*- coding: utf-8 -*-
"""
    views相关模块代码
"""
from rest_framework import viewsets
from rest_framework.views import APIView

from component.drf.mixins import ApiGenericMixin


class APIView(ApiGenericMixin, APIView):
    """APIView"""
    pass


class ModelViewSet(ApiGenericMixin, viewsets.ModelViewSet):
    """按需改造DRF默认的ModelViewSet类"""
    pass


class ReadOnlyModelViewSet(ApiGenericMixin, viewsets.ReadOnlyModelViewSet):
    """按需改造DRF默认的ModelViewSet类"""
    pass


class ViewSet(ApiGenericMixin, viewsets.ViewSet):
    """按需改造DRF默认的ViewSet类"""
    pass


class GenericViewSet(ApiGenericMixin, viewsets.GenericViewSet):
    """按需改造DRF默认的GenericViewSet类"""
    pass
