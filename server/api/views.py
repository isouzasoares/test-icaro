# -*- coding: utf-8 -*-

from rest_framework.generics import ListAPIView

from serializers import ProviderSerializer, SystemSerializer
from server.models import Provider, OperationSystem


class ProviderView(ListAPIView):
    model = Provider
    serializer_class = ProviderSerializer

    def get_queryset(self):
        return Provider.objects.all()


class SystemView(ListAPIView):
    model = OperationSystem
    serializer_class = SystemSerializer

    def get_queryset(self):
        return OperationSystem.objects.all()
