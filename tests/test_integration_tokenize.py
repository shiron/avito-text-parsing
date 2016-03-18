#coding=utf-8
from unittest import TestCase
from document import tokenize


class FraudTestCase(TestCase):
    """Integration test for tokenize document and detect fraud"""

    def test_tokenize_empty_doc(self):
        """emty doc"""
        data = u''
        is_fraud, tokens = tokenize(data)
        self.assertFalse(is_fraud, 'Fraud is True, but must be False')
        self.assertEqual([], tokens, 'Tokens is not empty')

    def test_tokenize_doc_with_one_good_word(self):
        """doc with one word"""
        data = u'красивый'
        is_fraud, tokens = tokenize(data)
        self.assertFalse(is_fraud, 'Fraud is True, but must be False')
        self.assertListEqual([u'красив'], tokens, 'Wrong tokens')

    def test_tokenize_doc_with_stop_words(self):
        """doc with one word"""
        data = u'и в к на'
        is_fraud, tokens = tokenize(data)
        self.assertFalse(is_fraud, 'Fraud is True, but must be False')
        self.assertListEqual([], tokens, 'Wrong tokens')

    def test_tokenize_doc_with_few_words(self):
        """doc with one word"""
        data = u'Я иду шагаю по Москве'
        is_fraud, tokens = tokenize(data)
        self.assertFalse(is_fraud, 'Fraud is True, but must be False')
        self.assertListEqual([u'ид', u'шага', u'москв'], tokens, 'Wrong tokens')

    def test_tokenize_fraud_doc_one_word(self):
        """doc with one word"""
        data = u'мучaчa'
        is_fraud, tokens = tokenize(data)
        self.assertTrue(is_fraud, 'Fraud is False, but must be True')
        self.assertListEqual([u'мучач'], tokens, 'Wrong tokens')

    def test_tokenize_fraud_doc_few_word(self):
        """doc with one word"""
        data = u'Рождeнный, пoлзать! (допoлзет)- до ;ручки'
        is_fraud, tokens = tokenize(data)
        self.assertTrue(is_fraud, 'Fraud is False, but must be True')
        self.assertListEqual([u'рожден', u'полза', u'доползет', u'ручк'], tokens, 'Wrong tokens')
