# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import ProviderView

urlpatterns = [
    url(r'^provider/list', ProviderView.as_view(), name='provider_list'),
]
