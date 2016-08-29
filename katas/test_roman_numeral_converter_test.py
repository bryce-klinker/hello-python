import unittest

from katas.roman_numeral_converter import RomanNumeralConverter


class RomanNumeralConverterTest(unittest.TestCase):
    def test_I_to_arabic_equals_1(self):
        converter = RomanNumeralConverter()
        result = converter.to_arabic('I')
        self.assertEquals(1, result)

    def test_II_to_arabic_equals_2(self):
        converter = RomanNumeralConverter()
        result = converter.to_arabic('II')
        self.assertEquals(2, result)

if __name__ == '__main__':
    unittest.main()