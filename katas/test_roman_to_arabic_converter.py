import unittest
from nose.tools import *

from katas.roman_numeral import RomanNumeral


class RomanToArabicConverterTest(unittest.TestCase):
    def test_I_to_arabic_equals_1(self):
        self.assert_roman_to_arabic("I", 1)

    def test_II_to_arabic_equals_2(self):
        self.assert_roman_to_arabic("II", 2)

    def test_III_to_arabic_equals_3(self):
        self.assert_roman_to_arabic("III", 3)

    def test_IV_to_arabic_equals_4(self):
        self.assert_roman_to_arabic("IV", 4)

    def test_V_to_arabic_equals_5(self):
        self.assert_roman_to_arabic("V", 5)

    def test_IX_to_arabic_equals_9(self):
        self.assert_roman_to_arabic("IX", 9)

    def test_X_to_arabic_equals_10(self):
        self.assert_roman_to_arabic("X", 10)

    def test_XL_to_arabic_equals_40(self):
        self.assert_roman_to_arabic("XL", 40)

    def test_XC_to_arabic_equals_90(self):
        self.assert_roman_to_arabic("XC", 90)

    def test_C_to_arabic_equals_100(self):
        self.assert_roman_to_arabic("C", 100)

    def test_CD_to_arabic_equals_400(self):
        self.assert_roman_to_arabic("CD", 400)

    def test_D_to_arabic_equals_500(self):
        self.assert_roman_to_arabic("D", 500)

    def test_CM_to_arabic_equals_900(self):
        self.assert_roman_to_arabic("CM", 900)

    def test_M_to_arabic_equals_1000(self):
        self.assert_roman_to_arabic("M", 1000)

    def test_MMMCMXCIX_to_arabic_equals_3999(self):
        self.assert_roman_to_arabic("MMMCMXCIX", 3999)

    @raises(RuntimeError)
    def test_IIII_to_arabic_raises_error(self):
        RomanNumeral.from_roman("IIII")

    @raises(RuntimeError)
    def test_XXXX_to_arabic_raises_error(self):
        RomanNumeral.from_roman("XXXX")

    @raises(RuntimeError)
    def test_CCCC_to_arabic_raises_error(self):
        RomanNumeral.from_roman("CCCC")

    @raises(RuntimeError)
    def test_MMMM_to_arabic_raises_error(self):
        RomanNumeral.from_roman("MMMM")

    @raises(RuntimeError)
    def test_IVIV_to_arabic_raises_error(self):
        RomanNumeral.from_roman("IVIV")

    @raises(RuntimeError)
    def test_VV_to_arabic_raises_error(self):
        RomanNumeral.from_roman("VV")

    @raises(RuntimeError)
    def test_IXIX_to_arabic_raises_error(self):
        RomanNumeral.from_roman("IXIX")

    @raises(RuntimeError)
    def test_XLXL_to_arabic_raises_error(self):
        RomanNumeral.from_roman("XLXL")

    @raises(RuntimeError)
    def test_LL_to_arabic_raises_error(self):
        RomanNumeral.from_roman("LL")

    @raises(RuntimeError)
    def test_XCXC_to_arabic_raises_error(self):
        RomanNumeral.from_roman("XCXC")

    @raises(RuntimeError)
    def test_CDCD_to_arabic_raises_error(self):
        RomanNumeral.from_roman("CDCD")

    @raises(RuntimeError)
    def test_DD_to_arabic_raises_error(self):
        RomanNumeral.from_roman("DD")

    @raises(RuntimeError)
    def test_CMCM_to_arabic_raises_error(self):
        RomanNumeral.from_roman("CMCM")

    def assert_roman_to_arabic(self, roman, arabic):
        result = RomanNumeral.from_roman(roman)
        self.assertEquals(arabic, result.arabic)