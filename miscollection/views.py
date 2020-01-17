# _*_ coding: utf-8 _*_
__author__ = 'fortune'
__date__ = '2019/10/18 23:20'

from rest_framework.response import Response
from miscollection.models import Mistake, Summary
from miscollection.serializers import MistakeSerializer, SummarySerializer
from component.drf import viewsets as component_viewsets
from django.db import transaction
from rest_framework.decorators import action

from miscollection.utils import get_children_data


class MistakeViewSet(component_viewsets.ModelViewSet):
    serializer_class = MistakeSerializer
    queryset = Mistake.objects.all().order_by("create_at")
    pagination_class = None
    permission_classes = ()

    filter_fields = {
    }

    @action(methods=['post'], detail=False)
    def batch_create(self, request):
        subjectList = request.data
        for subject in subjectList:
            obi, created = Mistake.objects.update_or_create(
                defaults={
                    'content': subject.get('subject', {}).get('content', ''),
                    'options': subject.get('options', []),
                },
                index=subject.get('subject', {}).get('index', ''),
                )
        return Response('ok')


class SummaryViewSet(component_viewsets.ModelViewSet):
    """服务目录视图"""

    serializer_class = SummarySerializer
    queryset = Summary.objects.filter(is_deleted=False).order_by('-create_at', 'level')
    filter_fields = {
    }

    @action(methods=['get'], detail=False)
    def get_mptt_summary(self, request):
        summarys = Summary.objects.all()
        root_summary = summarys.filter(level=0)[0]
        tree_data = {"data": {"text": root_summary.subject_title}, "children": []}
        get_children_data(root_summary, tree_data.get('children'))
        return Response(data=tree_data)

    @action(methods=['post'], detail=False)
    def batch_create(self, request):
        summaryList = request.data
        return Response('ok')
