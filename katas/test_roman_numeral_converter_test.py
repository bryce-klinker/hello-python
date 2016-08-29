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

    def test_IX_to_arabic_equals_9(self):
        result = self.converter.to_arabic('IX')
        self.assertEquals(9, result)

    def test_X_to_arabic_equals_10(self):
        result = self.converter.to_arabic('X')
        self.assertEquals(10, result)

    def test_1_to_roman_equals_I(self):
        result = self.converter.to_roman(1)
        self.assertEquals('I', result)

    def test_2_to_roman_equals_II(self):
        result = self.converter.to_roman(2)
        self.assertEquals('II', result)

if __name__ == '__main__':
    unittest.main()