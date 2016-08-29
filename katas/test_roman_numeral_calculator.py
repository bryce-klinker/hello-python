import unittest
from roman_numeral_calculator import RomanNumeralCalculator


class RomanNumeralCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = RomanNumeralCalculator()

    def test_I_plus_I_equals_II(self):
        result = self.calculator.add('I', 'I')
        self.assertEqual('II', result)

    def test_II_plus_I_equals_III(self):
        result = self.calculator.add('II', 'I')
        self.assertEqual('III', result)

    def test_I_plus_II_equals_III(self):
        result = self.calculator.add('I', 'II')
        self.assertEqual('III', result)

    def test_II_plus_II_equals_IV(self):
        result = self.calculator.add('II', 'II')
        self.assertEquals('IV', result)

    def test_IV_plus_I_equals_V(self):
        result = self.calculator.add('IV', 'I')
        self.assertEquals('V', result)

if __name__ == '__main__':
    unittest.main()
