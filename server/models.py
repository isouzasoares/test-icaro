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
    system = models.ForeignKey('OperationSystem')
    amount_of_cpu = models.PositiveSmallIntegerField(default=1,
                                                     verbose_name=u'CPUs')
    amount_of_memory = models.FloatField(verbose_name=u'Memory (GB)')
    amount_of_hd = models.FloatField(verbose_name=u'Hd (GB)')
    provider = models.ForeignKey('Provider')

    def __str__(self):
        return self.name
