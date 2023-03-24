import unittest
from unittest import TestCase
from main import city, geo_log

class TestCity(TestCase):
    #@unittest
    def test_city_list(self):
        result = city(geo_log)
        self.assertNotEquals(result, geo_log)

