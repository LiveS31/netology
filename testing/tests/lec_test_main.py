from unittest import TestCase

import pytest

from lec_main import summarize, multiply, get_dict

from random import randint, choice


# class TestSummarize(TestCase):
#     def test_2_positive_nums(self):
#         x, y = 10, 20
#         result = summarize(x, y)
#         expected = 30
#         self.assertEqual(result, expected)
#
#     def test_2_negative_nums(self):
#         x, y = 10, -20
#         expected = 30
#         result = summarize(x, y)
#         self.assertEqual(result, expected)
#
#     def test_not_in(self):
#         x = 20
#         y = 40
#         result = summarize(x, y)
#         expected = range(100, 200)
#         self.assertNotIn(result, expected)


# def get_random_numbers():
#     rand1 = randint(-100, 100)
#     rand2 = randint(-100, 100)
#     expected = rand1 * rand2
#     return rand1, rand2, expected


# class TestMultiply:
    # def test_2_nums(self):
    #     x, y = 20, 30
    #     result = multiply(x, y)
    #     expected = 600
    #     assert result == expected

    # @pytest.mark.parametrize(
    #     "x, y, expected", (
    #         (10, 20, 200),
    #         (9, 15, 135),
    #         (-10, 0.1, -1),
    #         (-20, -19, 380),
    #         (-94, 5, -470)
    #     )
    # )

    # @pytest.mark.parametrize(
    #     "x, y, expected", [get_random_numbers() for _ in range(5)]
    # )
    # def test_with_params(self, x, y, expected):
    #     print(x, y)
    #     result = multiply(x, y)
    #     assert result == expected
    #
    # def test_random_int(self):
    #     num = randint(1, 9)
    #     result = num ** 2
    #     assert result in range(1, 81)
    #
    #     rand1 = randint(1, 100)
    #     rand2 = randint(1, 100)
    #     expected = rand1 + rand2
    #     result = summarize(rand1, rand2)
    #     assert result == expected
    #
    # def test_not_equal(self):
    #     x = 10
    #     y = 20
    #     result = summarize(x, y)
    #     expected = range(2000, 5000)
    #     assert result not in expected


class TestGetDict(TestCase):
    def test_key_in_dict(self):
        keys = ['name', 'age', 'city']
        random_key = choice(keys)
        dict_ = get_dict()
        self.assertIn(random_key, dict_)

    def test_length(self):
        dict_ = get_dict()
        self.assertEqual(len(dict_), 3)

    def test_dict_equal(self):
        dict_ = get_dict()
        expected_dict = {'name': 'Makar', 'age': 30, 'city': 'Kazan'}
        self.assertSequenceEqual(dict_.keys(), expected_dict.keys())

   # def test_regex(self):
   #      test_string = '2022/04/30'
   #      pattern = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
   #      self.assertRegex(test_string, pattern)