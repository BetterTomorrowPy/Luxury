# -*- coding: utf-8 -*-
"""

"""
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_driver(self):
        self.driver.get('http://python.org')
        element = self.driver.find_element_by_name('p')
        element.clear()
        element.send_keys('pycon')
        element.send_keys(Keys.RETURN)
        self.assertIn('Python', self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()