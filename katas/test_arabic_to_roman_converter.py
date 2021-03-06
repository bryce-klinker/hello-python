import unittest
from nose.tools import *
from katas.roman_numeral import RomanNumeral


class ArabicToRomanConverterTest(unittest.TestCase):
    def test_1_to_roman_equals_I(self):
        self.assert_arabic_to_roman(1, "I")

    def test_2_to_roman_equals_II(self):
        self.assert_arabic_to_roman(2, "II")

    def test_3_to_roman_equals_III(self):
        self.assert_arabic_to_roman(3, "III")

    def test_4_to_roman_equals_IV(self):
        self.assert_arabic_to_roman(4, "IV")

    def test_5_to_roman_equals_V(self):
        self.assert_arabic_to_roman(5, "V")

    def test_9_to_roman_equals_IX(self):
        self.assert_arabic_to_roman(9, "IX")

    def test_10_to_roman_equals_X(self):
        self.assert_arabic_to_roman(10, "X")

    def test_20_to_roman_equals_XX(self):
        self.assert_arabic_to_roman(20, "XX")

    def test_40_to_roman_equals_XL(self):
        self.assert_arabic_to_roman(40, "XL")

    def test_50_to_roman_equals_L(self):
        self.assert_arabic_to_roman(50, "L")

    def test_90_to_roman_equals_XC(self):
        self.assert_arabic_to_roman(90, "XC")

    def test_100_to_roman_equals_C(self):
        self.assert_arabic_to_roman(100, "C")

    def test_400_to_roman_equals_CD(self):
        self.assert_arabic_to_roman(400, "CD")

    def test_500_to_roman_equals_D(self):
        self.assert_arabic_to_roman(500, "D")

    def test_900_to_roman_equals_CM(self):
        self.assert_arabic_to_roman(900, "CM")

    def test_1000_to_roman_equals_M(self):
        self.assert_arabic_to_roman(1000, "M")

    @raises(RuntimeError)
    def test_4000_to_roman_raises_error(self):
        RomanNumeral.from_arabic(4000)

    @raises(RuntimeError)
    def test_negative_1_to_roman_raises_error(self):
        RomanNumeral.from_arabic(-1)

    @raises(RuntimeError)
    def test_0_to_roman_raises_error(self):
        RomanNumeral.from_arabic(0)

    def assert_arabic_to_roman(self, arabic, roman):
        result = RomanNumeral.from_arabic(arabic)
        self.assertEquals(roman, result.roman)
