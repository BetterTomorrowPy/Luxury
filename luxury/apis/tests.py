# -*- coding: utf-8 -*-
"""
    test.
"""
from django.test import TestCase
from django.db import models


class Animal(models.Model):
    """"""
    name = models.CharField('名字', max_length=64)
    sound = models.CharField(max_length=64, blank=True, default='')

    def speak(self):
        return self.sound


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name='lion', sound='roar')
        Animal.objects.create(name='cat', sound='meow')

    def test_animals_can_speak(self):
        lino = Animal.objects.get(name='lino')
        cat = Animal.objects.get(name='cat')
        self.assertEqual(lino.speak(), 'roar')
        self.assertEqual(cat.speak(), 'meow')
