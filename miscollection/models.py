# -*- coding: utf-8 -*-
import jsonfield

from django.db import models, transaction
from miscollection import managers
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
from component.constants import (
    DEFAULT_ORDER,
    DEFAULT_STRING,
    DEFAULT_VERSION,
    EMPTY_DICT,
    EMPTY_INT,
    EMPTY_LIST,
    EMPTY_STRING,
    LEN_LONG,
    LEN_DESC,
    LEN_MIDDLE,
    LEN_NORMAL,
    LEN_SHORT,
    LEN_X_LONG,
    LEN_XX_LONG,
    LEN_XXX_LONG,
)


class Model(models.Model):
    """基础字段"""

    FIELDS = ('creator', 'create_at', 'updated_by', 'update_at')

    create_at = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_at = models.DateTimeField(u"更新时间", auto_now=True)
    is_deleted = models.BooleanField(u"是否软删除", default=False, db_index=True)
    _objects = models.Manager()
    objects = models.Manager()

    class Meta:
        app_label = 'miscollection'
        abstract = True

    def delete(self, using=None):
        self.is_deleted = True
        self.save()

    def hard_delete(self, using=None):
        super(Model, self).delete()


class Mistake(Model):
    index = models.CharField(u"题号", max_length=LEN_SHORT, default=u'')
    content = models.CharField(u"题目", max_length=LEN_X_LONG, default=u'')
    options = jsonfield.JSONField(u"选项内容", max_length=LEN_X_LONG)

    objects = managers.Manager()

    class Meta:
        app_label = "miscollection"
        verbose_name = u"错题"
        verbose_name_plural = verbose_name


class BaseMpttModel(MPTTModel):
    """基础字段"""

    FIELDS = ('creator', 'create_at', 'updated_by', 'update_at', 'end_at')

    creator = models.CharField(u"创建人", max_length=LEN_NORMAL, null=True, blank=True, default='system')
    create_at = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_at = models.DateTimeField(u"更新时间", auto_now=True)
    updated_by = models.CharField(u"修改人", max_length=LEN_NORMAL, null=True, blank=True, default='system')
    end_at = models.DateTimeField(u"结束时间", null=True, blank=True)
    is_deleted = models.BooleanField(u"是否软删除", default=False, db_index=True)

    _objects = TreeManager()
    objects = managers.BaseTreeManager()

    class Meta:
        app_label = 'miscollection'
        abstract = True

    def delete(self, using=None):
        self.is_deleted = True
        self.save()

    def hard_delete(self, using=None):
        super(BaseMpttModel, self).delete()


class Summary(BaseMpttModel):
    id = models.CharField("ID", max_length=80, primary_key=True)
    subject_title = models.CharField(u"科目名称", max_length=LEN_NORMAL, default=u'')
    chapter = models.CharField(u"章节号", max_length=LEN_SHORT, default=u'')
    content = models.CharField(u"总结内容", max_length=LEN_X_LONG, default=u'')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name=u"上一目录",
        null=True,
        blank=True,
        related_name='children'
    )

    objects = managers.Manager()

    class Meta:
        app_label = "miscollection"
        verbose_name = u"总结"
        verbose_name_plural = verbose_name
