# -*- coding: utf-8 -*-
import datetime

from django.utils import timezone


def now():
    """
    返回当前时间
    """
    return timezone.now()


def time_delta(hours=1, minutes=30):
    """
    时间间隔
    """
    return datetime.timedelta(hours=hours, minutes=minutes)


def index_of_list(objarr, key, val):
    """
    根据对象的某一属性寻找对象在其所在列表中的位置
    """
    return next((k for k, v in enumerate(objarr) if v[key] == val), -1)