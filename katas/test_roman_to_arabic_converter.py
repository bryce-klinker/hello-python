import unittest

from katas.roman_numeral import RomanNumeral


class RomanToArabicConverterTest(unittest.TestCase):
    def test_I_to_arabic_equals_1(self):
        result = RomanNumeral.from_roman('I')
        self.assertEquals(1, result.arabic)

    def test_II_to_arabic_equals_2(self):
        result = RomanNumeral.from_roman('II')
        self.assertEquals(2, result.arabic)

    def test_III_to_arabic_equals_3(self):
        result = RomanNumeral.from_roman('III')
        self.assertEquals(3, result.arabic)

    def test_IV_to_arabic_equals_4(self):
        result = RomanNumeral.from_roman('IV')
        self.assertEquals(4, result.arabic)

    def test_V_to_arabic_equals_5(self):
        result = RomanNumeral.from_roman('V')
        self.assertEquals(5, result.arabic)

    def test_IX_to_arabic_equals_9(self):
        result = RomanNumeral.from_roman('IX')
        self.assertEquals(9, result.arabic)

    def test_X_to_arabic_equals_10(self):
        result = RomanNumeral.from_roman('X')
        self.assertEquals(10, result.arabic)
