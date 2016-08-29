import unittest

from katas.arabic_to_roman_converter import arabic_to_roman


class ArabicToRomanConverterTest(unittest.TestCase):
    def test_1_to_roman_equals_I(self):
        result = arabic_to_roman(1)
        self.assertEquals('I', result)

    def test_2_to_roman_equals_II(self):
        result = arabic_to_roman(2)
        self.assertEquals('II', result)

    def test_3_to_roman_equals_III(self):
        result = arabic_to_roman(3)
        self.assertEquals('III', result)

    def test_4_to_roman_equals_IV(self):
        result = arabic_to_roman(4)
        self.assertEquals('IV', result)

    def test_5_to_roman_equals_V(self):
        result = arabic_to_roman(5)
        self.assertEquals('V', result)


if __name__ == '__main__':
    unittest.main()