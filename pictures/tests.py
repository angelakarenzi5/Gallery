from django.test import TestCase
from .models import Image,Category,Location

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wecode= Location(city = 'Kigali', country ='Rwanda')
