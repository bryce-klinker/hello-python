import unittest
from roman_numeral_calculator import RomanNumeralCalculator

class RomanNumeralCalculatorTest(unittest.TestCase):
    def test_I_plus_I_equals_II(self):
        calculator = RomanNumeralCalculator()
        result = calculator.add('I', 'I')
        self.assertEqual('II', result)


if __name__ == '__main__':
    unittest.main()
