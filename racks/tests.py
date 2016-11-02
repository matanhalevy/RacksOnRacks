__author__ = 'jonathanhansen'

from django.test import TestCase
from models import BikeRack

class BikeRackTestCase(TestCase):
    def setUp(self):
        BikeRack.objects.create(address="Meow Mix", number=2000, lat=12.34, lon=-600.00, skytrain="mile high")

    def test_create(self):
        rack = BikeRack.objects.get(address="Meow Mix")

        self.assertEquals(rack.address, "Meow Mix")
        self.assertEquals(rack.number, 2000)
        self.assertEquals(rack.lat, 12.34)
        self.assertEquals(rack.lon, -600.00)
        self.assertEquals(rack.skytrain, "mile high")
