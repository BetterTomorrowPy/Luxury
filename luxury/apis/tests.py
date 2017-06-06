# -*- coding: utf-8 -*-
"""
    test.
"""
from django.test import TestCase

from .models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name='lion', sound='roar')
        Animal.objects.create(name='cat', sound='meow')

    def test_animals_can_speak(self):
        lino = Animal.objects.get(name='lino')
        cat = Animal.objects.get(name='cat')
        self.assertEqual(lino.speak(), 'roar')
        self.assertEqual(cat.speak(), 'meow')
