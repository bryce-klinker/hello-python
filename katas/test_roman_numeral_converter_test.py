import unittest

from katas.roman_numeral_converter import RomanNumeralConverter


class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        self.converter = RomanNumeralConverter()

    def test_I_to_arabic_equals_1(self):
        result = self.converter.to_arabic('I')
        self.assertEquals(1, result)

    def test_II_to_arabic_equals_2(self):
        result = self.converter.to_arabic('II')
        self.assertEquals(2, result)

    def test_III_to_arabic_equals_3(self):
        result = self.converter.to_arabic('III')
        self.assertEquals(3, result)

    def test_IV_to_arabic_equals_4(self):
        result = self.converter.to_arabic('IV')
        self.assertEquals(4, result)

if __name__ == '__main__':
    unittest.main()