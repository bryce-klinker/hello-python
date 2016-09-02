import unittest
from nose.tools import *
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

    def test_XL_plus_L_equals_L(self):
        self.assert_add_equals("XL", "L", "XC")

    def test_L_plus_L_equals_C(self):
        self.assert_add_equals("L", "L", "C")

    def test_C_plus_CCC_equals_CD(self):
        self.assert_add_equals("C", "CCC", "CD")

    def test_CCC_plus_CC_equals_D(self):
        self.assert_add_equals("CCC", "CC", "D")

    def test_D_plus_CD_equals_CM(self):
        self.assert_add_equals("D", "CD", "CM")

    def test_D_plus_D_equals_M(self):
        self.assert_add_equals("D", "D", "M")

    def test_II_minus_I_equals_I(self):
        self.assert_minus_equals("II", "I", "I")

    def test_V_minus_I_equals_IV(self):
        self.assert_minus_equals("V", "I", "IV")

    def test_X_minus_I_equals_IX(self):
        self.assert_minus_equals("X", "I", "IX")

    def test_C_minus_I_equals_XCIX(self):
        self.assert_minus_equals("C", "I", "XCIX")

    def test_M_minus_I_equals_CMXCIX(self):
        self.assert_minus_equals("M", "I", "CMXCIX")

    def test_M_minus_C_equals_CM(self):
        self.assert_minus_equals("M", "C", "CM")

    @raises(RuntimeError)
    def test_MMM_plus_M_throws_runtime_error(self):
        self.calculator.add("MMM", "M")

    def assert_add_equals(self, first, second, expected):
        actual = self.calculator.add(first, second)
        self.assertEquals(expected, actual)

    def assert_minus_equals(self, first, second, expected):
        actual = self.calculator.subtract(first, second)
        self.assertEquals(expected, actual)