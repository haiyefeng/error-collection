# _*_ coding: utf-8 _*_
__author__ = 'fortune'
__date__ = '2019/12/27 11:06'
from rest_framework import serializers
from rest_framework.fields import JSONField, empty

from miscollection.models import Mistake, Summary

from component.constants import (
    LEN_X_LONG,
    LEN_LONG
)

class MistakeSerializer(serializers.ModelSerializer):
    """错题"""
    options = JSONField(required=True)

    class Meta:
        model = Mistake
        fields = "__all__"

    def to_representation(self, instance):
        data = super(MistakeSerializer, self).to_representation(instance)
        error_dict = {
            'subject': {'index': data.get('index', ''), 'content': data.get('content', '')},
            'options': data.get('options', []),
        }
        return error_dict


class SummarySerializer(serializers.ModelSerializer):
    """服务目录序列化"""

    level = serializers.IntegerField(required=False, min_value=0)
    subject_title = serializers.CharField(required=True,
                                 error_messages={'blank': u"科目不能为空"},
                                 max_length=LEN_LONG)
    chapter = serializers.CharField(required=True,
                                 error_messages={'blank': u"科目不能为空"},
                                 max_length=LEN_LONG)
    # allow_blank -> 允许字段为空字符串
    content = serializers.CharField(required=False, max_length=LEN_X_LONG, allow_blank=True)

    class Meta:
        model = Summary
        fields = (
            "id",
            "level",
            "parent",
            "subject_title",
            "chapter",
            "content",
        )
        # 只读字段在创建和更新时均被忽略
        read_only_fields = (
            "id",
            "key",
            "parent_name",
            "parent_key",
            "parent__id",
            "parent__name",
        )
