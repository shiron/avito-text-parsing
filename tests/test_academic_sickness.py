#coding=utf-8
from unittest import TestCase
from document import academic_sickness


class FraudTestCase(TestCase):
    """Test for calculate academic sickness"""

    def test_ac_empty(self):
        """emty list"""
        data = []
        ac = academic_sickness(data)
        self.assertEqual(0, ac, 'Wrong value ac, expected {0}, but return {1}'.format(0, ac))

    def test_ac_one_token(self):
        """list with 1 word (less then 5)"""
        data = [u'адын']
        ac = academic_sickness(data)
        self.assertEqual(1, ac, 'Wrong value ac, expected {0}, but return {1}'.format(1, ac))

    def test_ac_five_token(self):
        """list with 5 word"""
        data = [u'адын', u'два', u'два', u'тры', u'четыря']
        ac = academic_sickness(data)
        self.assertEqual(1, ac, 'Wrong value ac, expected {0}, but return {1}'.format(1, ac))

    def test_ac_more_than_five_token_1(self):
        """list with 5 word"""
        data = [u'адын', u'два', u'два', u'тры', u'четыря', u'четыря']
        ac = academic_sickness(data)
        self.assertEqual(1, ac, 'Wrong value ac, expected {0}, but return {1}'.format(1, ac))

    def test_ac_more_than_five_token_05(self):
        """list with 5 word"""
        data = [u'адын', u'два', u'тры', u'четыря', u'пять', u'6', u'7', u'8', u'9', u'10']
        ac = academic_sickness(data)
        self.assertEqual(0.5, ac, 'Wrong value ac, expected {0}, but return {1}'.format(0.5, ac))