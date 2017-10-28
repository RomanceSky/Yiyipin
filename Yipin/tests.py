from django.test import TestCase
from TestApp.models import *
from django.utils import timezone
from django.core.urlresolvers import reverse
#from whatever.forms import WhateverForm


# model test

class WhateverTest(TestCase):
    def create_whatever(self, title="only a test", body="yes, this is only a test"):
        return whatever.objects.create(title=title, body=body, created_at=timezone.now())

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, whatever))
        self.assertEqual(w.__unicode__(), w.title)

