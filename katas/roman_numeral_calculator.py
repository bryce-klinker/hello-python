from katas.roman_to_arabic_converter import roman_to_arabic
from katas.arabic_to_roman_converter import arabic_to_roman

class RomanNumeralCalculator(object):
    def add(self, first, second):
        first_arabic = roman_to_arabic(first)
        second_arabic = roman_to_arabic(second)
        arabic_result = first_arabic + second_arabic
        return arabic_to_roman(arabic_result)
