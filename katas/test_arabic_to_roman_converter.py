import unittest

from katas.arabic_to_roman_converter import arabic_to_roman


class ArabicToRomanConverterTest(unittest.TestCase):
    def test_1_to_roman_equals_I(self):
        result = arabic_to_roman(1)
        self.assertEquals('I', result)

    def test_2_to_roman_equals_II(self):
        result = arabic_to_roman(2)
        self.assertEquals('II', result)

if __name__ == '__main__':
    unittest.main()