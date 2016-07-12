from django.test import TestCase

from models import Provider, OperationSystem

# Create your tests here.


class ServerTestCase(TestCase):

    def setUp(self):
        """start test object"""
        Provider.objects.create(name='Amazon')
        OperationSystem.objects.create(name='Windows')

    def teste_get_object(self):

        provider = Provider.objects.get(name='Amazon')
        system = OperationSystem.objects.get(name='Windows')
        self.assertEqual(provider.name, 'Amazon')
        self.assertEqual(system.name, 'Windows')
