import unittest
from roman_numeral_calculator import RomanNumeralCalculator


class RomanNumeralCalculatorTest(unittest.TestCase):
    def test_I_plus_I_equals_II(self):
        calculator = RomanNumeralCalculator()
        result = calculator.add('I', 'I')
        self.assertEqual('II', result)

    def test_II_plus_I_equals_III(self):
        calculator = RomanNumeralCalculator()
        result = calculator.add('II', 'I')
        self.assertEqual('III', result)

    def test_I_plus_II_equals_III(self):
        calculator = RomanNumeralCalculator()
        result = calculator.add('I', 'II')
        self.assertEqual('III', result)

if __name__ == '__main__':
    unittest.main()
