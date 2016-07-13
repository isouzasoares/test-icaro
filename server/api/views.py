# -*- coding: utf-8 -*-

from rest_framework.generics import ListAPIView

from serializers import (ProviderSerializer, SystemSerializer,
                         HardDiskSerializer, InstanceSerializer)

from server.models import Provider, OperationSystem, HardDisk, Instance


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


class HardDiskView(ListAPIView):
    model = HardDisk
    serializer_class = HardDiskSerializer

    def get_queryset(self):
        return HardDisk.objects.all()


class InstanceView(ListAPIView):
    model = Instance
    serializer_class = InstanceSerializer

    def get_queryset(self):
        return Instance.objects.all()
