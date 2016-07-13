# -*- coding: utf-8 -*-

from rest_framework import serializers
from server.models import Provider


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'
