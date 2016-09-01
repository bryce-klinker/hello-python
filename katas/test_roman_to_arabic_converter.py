import unittest

from katas.roman_numeral import RomanNumeral


class RomanToArabicConverterTest(unittest.TestCase):
    def test_I_to_arabic_equals_1(self):
        self.assert_roman_to_arabic("I", 1)

    def test_II_to_arabic_equals_2(self):
        self.assert_roman_to_arabic("II", 2)

    def test_III_to_arabic_equals_3(self):
        self.assert_roman_to_arabic("III", 3)

    def test_IV_to_arabic_equals_4(self):
        self.assert_roman_to_arabic("IV", 4)

    def test_V_to_arabic_equals_5(self):
        self.assert_roman_to_arabic("V", 5)

    def test_IX_to_arabic_equals_9(self):
        self.assert_roman_to_arabic("IX", 9)

    def test_X_to_arabic_equals_10(self):
        self.assert_roman_to_arabic("X", 10)

    def test_XL_to_arabic_equals_40(self):
        self.assert_roman_to_arabic("XL", 40)

    def test_XC_to_arabic_equals_90(self):
        self.assert_roman_to_arabic("XC", 90)

    def test_C_to_arabic_equals_100(self):
        self.assert_roman_to_arabic("C", 100)

    def test_CD_to_arabic_equals_400(self):
        self.assert_roman_to_arabic("CD", 400)

    def assert_roman_to_arabic(self, roman, arabic):
        result = RomanNumeral.from_roman(roman)
        self.assertEquals(arabic, result.arabic)