from django.test import TestCase
from .models import Organization
from datetime import date

class OrganizationModelTest(TestCase):
    def test_str_method(self):
        org = Organization(name='UFC', founded=date(1993,11,12), country='USA')
        self.assertEqual(str(org), 'UFC')
