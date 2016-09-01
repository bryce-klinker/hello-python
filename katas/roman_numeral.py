from katas.roman_to_arabic_converter import roman_to_arabic
from katas.arabic_to_roman_converter import arabic_to_roman


class RomanNumeral:
    def __init__(self, roman):
        self._roman = roman

    @property
    def roman(self):
        return self._roman

    @property
    def arabic(self):
        return roman_to_arabic(self._roman)

    def add(self, roman_numeral):
        arabic_sum = self.arabic + roman_numeral.arabic
        roman_sum = arabic_to_roman(arabic_sum)
        return RomanNumeral(roman_sum)
