from roman_numeral import RomanNumeral


class RomanNumeralCalculator(object):
    def add(self, first, second):
        first_roman_numeral = RomanNumeral(first)
        second_roman_numeral = RomanNumeral(second)
        sum_roman_numeral = first_roman_numeral.add(second_roman_numeral)
        return sum_roman_numeral.roman

    def subtract(self, first, second):
        first_roman_numeral = RomanNumeral(first)
        second_roman_numeral = RomanNumeral(second)
        difference = first_roman_numeral.minus(second_roman_numeral)
        return difference.roman
