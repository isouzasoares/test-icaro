# -*- coding: utf-8 -*-

from rest_framework import serializers
from server.models import Provider, OperationSystem


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'


class SystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperationSystem
        fields = '__all__'
