import unittest

class RomanNumeralConverterTest(unittest.TestCase):
    def test_I_to_arabic_equals_1(self):
        converter = RomanNumeralConverter()
        result = converter.to_arabic('I')
        self.assertEquals(1, result)


if __name__ == '__main__':
    unittest.main()