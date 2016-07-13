# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import ProviderView, SystemView

urlpatterns = [
    url(r'^provider/list', ProviderView.as_view(), name='provider_list'),
    url(r'^system/list', SystemView.as_view(), name='system_list'),
]
