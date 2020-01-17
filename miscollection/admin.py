# -*- coding: utf-8 -*-
from django.contrib import admin
from miscollection.models import Mistake, Summary
# Register your models here.


admin.site.register([Mistake, Summary])