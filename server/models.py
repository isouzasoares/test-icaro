from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.


@python_2_unicode_compatible
class Provider(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class OperationSystem(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Instance(models.Model):

    name = models.CharField(max_length=256)
    amount_of_cpu = models.PositiveSmallIntegerField(default=1)
    amount_of_memory = models.FloatField()
    amount_of_hd = models.FloatField()
    provider = models.ForeignKey('Provider')
    system = models.ForeignKey('OperationSystem')

    def __str__(self):
        return self.name
