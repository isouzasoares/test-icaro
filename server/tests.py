from django.test import TestCase

from models import Provider, OperationSystem, Instance, HardDisk

# Create your tests here.


class ServerTestCase(TestCase):

    def setUp(self):
        """start test object"""
        Provider.objects.create(name='Amazon')
        OperationSystem.objects.create(name='Windows')
        HardDisk.objects.create(hd_type='ssd', amount_of_hd=40.0)

    def teste_get_object(self):

        provider = Provider.objects.get(name='Amazon')
        system = OperationSystem.objects.get(name='Windows')
        hd = HardDisk.objects.get(hd_type='ssd')
        self.assertEqual(provider.name, 'Amazon')
        self.assertEqual(system.name, 'Windows')
        self.assertEqual(hd.__str__(), '40.0 ssd')

    def test_add_instance_object(self):

        provider = Provider.objects.get(name='Amazon')
        system = OperationSystem.objects.get(name='Windows')
        Instance.objects.create(name='Instance1',
                                amount_of_cpu=2,
                                amount_of_memory=256,
                                provider=provider,
                                price=49.00,
                                system=system)
        instance = Instance.objects.filter(provider=provider,
                                           system=system)
        self.assertEqual(len(instance), 1)
        self.assertEqual(len(instance.filter(price__gte=40)), 1)
