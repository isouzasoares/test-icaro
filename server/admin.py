# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Provider, OperationSystem, Instance

# Register your models here.
admin.site.register(Provider)
admin.site.register(OperationSystem)
admin.site.register(Instance)
