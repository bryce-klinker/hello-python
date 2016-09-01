import unittest

from katas.roman_numeral import RomanNumeral


class ArabicToRomanConverterTest(unittest.TestCase):
    def test_1_to_roman_equals_I(self):
        result = RomanNumeral.from_arabic(1)
        self.assertEquals('I', result.roman)

    def test_2_to_roman_equals_II(self):
        result = RomanNumeral.from_arabic(2)
        self.assertEquals('II', result.roman)

    def test_3_to_roman_equals_III(self):
        result = RomanNumeral.from_arabic(3)
        self.assertEquals('III', result.roman)

    def test_4_to_roman_equals_IV(self):
        result = RomanNumeral.from_arabic(4)
        self.assertEquals('IV', result.roman)

    def test_5_to_roman_equals_V(self):
        result = RomanNumeral.from_arabic(5)
        self.assertEquals('V', result.roman)

    def test_9_to_roman_equals_IX(self):
        result = RomanNumeral.from_arabic(9)
        self.assertEquals('IX', result.roman)

    def test_10_to_roman_equals_X(self):
        result = RomanNumeral.from_arabic(10)
        self.assertEquals('X', result.roman)

    def test_20_to_roman_equals_XX(self):
        result = RomanNumeral.from_arabic(20)
        self.assertEquals('XX', result.roman)

    def test_40_to_roman_equals_XL(self):
        result = RomanNumeral.from_arabic(40)
        self.assertEquals("XL", result.roman)

if __name__ == '__main__':
    unittest.main()