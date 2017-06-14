# -*- coding: utf-8 -*-
"""
    test.
"""
import torndb
import unittest

from ..views import case


class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """"""
        self.assertTrue(case.is_prime(2), msg='断言出错')


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = 'widget'
        self.db = torndb.Connection()

    def tearDown(self):
        self.db.close()



if __name__ == '__main__':
    unittest.main()
