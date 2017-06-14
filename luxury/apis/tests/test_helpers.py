# -*- coding: utf-8 -*-
"""

"""
from datetime import datetime

from django.test import TestCase
from voluptuous import *

print(locals())


schema = Schema({
    'q': str,
    'page': int,
    'page_size': int
})


