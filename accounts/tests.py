from django.test import TestCase
from .models import Interest

class InterestModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Interest.objects.create(name='Test Interest')

    def test_name_label(self):
        interest = Interest.objects.get(id=1)
        field_label = interest._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        interest = Interest.objects.get(id=1)
        max_length = interest._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_name_content(self):
        interest = Interest.objects.get(id=1)
        expected_object_name = f'{interest.name}'
        self.assertEqual(expected_object_name, str(interest))