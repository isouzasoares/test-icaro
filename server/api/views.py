# -*- coding: utf-8 -*-

from rest_framework.generics import ListAPIView

from serializers import ProviderSerializer
from server.models import Provider


class ProviderView(ListAPIView):
    model = Provider
    serializer_class = ProviderSerializer

    def get_queryset(self):
        return Provider.objects.all()
