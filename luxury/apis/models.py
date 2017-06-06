# -*- coding: utf-8 -*-
"""
    django test.
"""

from django.db import models


class Animal(models.Model):
    """"""
    name = models.CharField('名字', max_length=64)
    sound = models.CharField(max_length=64, blank=True, default='')

    def speak(self):
        return self.sound
