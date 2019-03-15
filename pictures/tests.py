from django.test import TestCase
from .models import Image,Category,Location

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wecode= Location(city = 'Kigali', country ='Rwanda')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Location))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)