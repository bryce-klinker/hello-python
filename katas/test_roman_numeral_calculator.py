import unittest
from roman_numeral_calculator import RomanNumeralCalculator


class RomanNumeralCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = RomanNumeralCalculator()

    def test_I_plus_I_equals_II(self):
        self.assert_add_equals("I", "I", "II")

    def test_II_plus_I_equals_III(self):
        self.assert_add_equals("II", "I", "III")

    def test_I_plus_II_equals_III(self):
        self.assert_add_equals("I", "II", "III")

    def test_II_plus_II_equals_IV(self):
        self.assert_add_equals("II", "II", "IV")

    def test_IV_plus_I_equals_V(self):
        self.assert_add_equals("IV", "I", "V")

    def test_I_plus_IV_equals_V(self):
        self.assert_add_equals("I", "IV", "V")

    def test_V_plus_V_equals_X(self):
        self.assert_add_equals("V", "V", "X")

    def test_IX_plus_I_equals_X(self):
        self.assert_add_equals("IX", "I", "X")

    def test_X_plus_XXX_equals_XL(self):
        self.assert_add_equals("X", "XXX", "XL")

    def test_XX_plus_XXX_equals_L(self):
        self.assert_add_equals("XX", "XXX", "L")

    def assert_add_equals(self, first, second, expected):
        actual = self.calculator.add(first, second)
        self.assertEquals(expected, actual)
