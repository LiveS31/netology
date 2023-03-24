import unittest
from unittest import TestCase
from main import city, geo_log, summ, ids


class TestCity(TestCase):
    def test_city_list(self):
        result = city(geo_log)# загоняем в переменную функцию, которую нужно вызвать
        finish_geo_log = ['Москва', 'Владимир', 'Тула', 'Тула', 'Курск', 'Архангельск']
        #в переменную то что нужно получиь в ответе
        assert result == finish_geo_log # самое сравнение


    def test_city_lists(self):
        result = city(geo_log) # загоняем в переменную функцию, которую нужно вызвать
        finish_geo_log = ['Москва', 'Владимир', 'Тула', 'Тула', 'Курск', 'Архангельск']
        self.assertEqual(result, finish_geo_log)# тоже самое


    def test_len_list(self):
        result = len(summ(ids))
        expected = 6
        self.assertEqual(result, expected)

