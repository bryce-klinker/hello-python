import unittest

from katas.roman_to_arabic_converter import to_arabic

class RomanToArabicConverterTest(unittest.TestCase):
    def test_I_to_arabic_equals_1(self):
        result = to_arabic('I')
        self.assertEquals(1, result)

    def test_II_to_arabic_equals_2(self):
        result = to_arabic('II')
        self.assertEquals(2, result)

    def test_III_to_arabic_equals_3(self):
        result = to_arabic('III')
        self.assertEquals(3, result)

    def test_IV_to_arabic_equals_4(self):
        result = to_arabic('IV')
        self.assertEquals(4, result)

    def test_IX_to_arabic_equals_9(self):
        result = to_arabic('IX')
        self.assertEquals(9, result)

    def test_X_to_arabic_equals_10(self):
        result = to_arabic('X')
        self.assertEquals(10, result)