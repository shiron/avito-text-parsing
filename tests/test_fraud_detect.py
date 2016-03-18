#coding=utf-8
from unittest import TestCase
from word import detect_fraud


class FraudTestCase(TestCase):
    """Test for fraud detect and recovery word"""

    def test_fraud_in_start_one_symbol(self):
        """aвокадо (Авокадо)"""
        is_fraud, word = detect_fraud(u'aвокадо')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'авокадо', word, 'Wrong replace symbols')

    def test_fraud_in_start_few_symbols(self):
        """артишок (АРтишок)"""
        is_fraud, word = detect_fraud(u'apтишок')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'артишок', word, 'Wrong replace symbols')

    def test_fraud_in_end_one_symbol(self):
        """почта (почтА)"""
        is_fraud, word = detect_fraud(u'почтa')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'почта', word, 'Wrong replace symbols')

    def test_fraud_in_end_few_symbols(self):
        """пожар (пожAP)"""
        is_fraud, word = detect_fraud(u'пожap')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'пожар', word, 'Wrong replace symbols')

    def test_fraud_in_middle_one_symbol(self):
        """печенька (печЕнька)"""
        is_fraud, word = detect_fraud(u'печeнька')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'печенька', word, 'Wrong replace symbols')

    def test_fraud_in_middle_few_symbols(self):
        """мизеришко (мизЕРишко)"""
        is_fraud, word = detect_fraud(u'мизepишко')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'мизеришко', word, 'Wrong replace symbols')

    def test_fraud_in_middle_twice(self):
        """пeченька (пEчЕнька)"""
        is_fraud, word = detect_fraud(u'пeчeнька')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'печенька', word, 'Wrong replace symbols')

    def test_fraud_in_middle_few_times_few_symbols(self):
        """сборнаяроссиипофутболу (сбОРнаярОссиипОфутболу)"""
        is_fraud, word = detect_fraud(u'сбopнаярoссиипoфутболу')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'сборнаяроссиипофутболу', word, 'Wrong replace symbols')

    def test_fraud_in_all_parts_of_word(self):
        """сборнаяроссиипофутболуест123-256_328печеньку (CбОРнаярОссиипОфутболуЕСт123-256_328печЕнькУ)"""
        is_fraud, word = detect_fraud(u'cбopнаярoссиипoфутболуecт123-256_328печeнькy')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'сборнаяроссиипофутболуест123-256_328печеньку', word, 'Wrong replace symbols')

    def test_good_latin(self):
        """LaserJet"""
        is_fraud, word = detect_fraud('laserjet')
        self.assertFalse(is_fraud, 'Wrong detect fraud')
        self.assertEqual('laserjet', word, 'Wrong replace symbols')

    def test_good_latin_and_cyrilic_1(self):
        """Cam-модуль"""
        is_fraud, word = detect_fraud(u'cam-модуль')
        self.assertFalse(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'cam-модуль', word, 'Wrong replace symbols')

    def test_good_latin_and_cyrilic_2(self):
        """Camмодуль"""
        is_fraud, word = detect_fraud(u'camмодуль')
        self.assertFalse(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'camмодуль', word, 'Wrong replace symbols')

    def test_good_num_and_latin(self):
        """rbc30set"""
        is_fraud, word = detect_fraud(u'rbc30set')
        self.assertFalse(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'rbc30set', word, 'Wrong replace symbols')

    def test_good_num_and_cyrilic(self):
        """30-летний"""
        is_fraud, word = detect_fraud(u'30-летний')
        self.assertFalse(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'30-летний', word, 'Wrong replace symbols')

    def test_good_num_and_cyrilic(self):
        """30летний"""
        is_fraud, word = detect_fraud(u'30летний')
        self.assertFalse(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'30летний', word, 'Wrong replace symbols')

    def test_fraud_cyrilic_and_latin(self):
        """почкa (почкА)"""
        is_fraud, word = detect_fraud(u'почкa')
        self.assertTrue(is_fraud, 'Wrong detect fraud')
        self.assertEqual(u'почка', word, 'Wrong replace symbols')
