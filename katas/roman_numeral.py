import operator


class Roman_Map:
    def __init__(self, symbol, arabic, max):
        self.symbol = symbol
        self.max = max
        self.arabic = arabic


class RomanNumeral:
    @property
    def roman(self):
        return self._roman

    @property
    def arabic(self):
        return RomanNumeral.convert_to_arabic(self.roman)

    def __init__(self, roman):
        if not RomanNumeral.is_valid_roman(roman):
            raise RuntimeError("The roman numeral " + roman + " is not valid")

        self._roman = roman

    def add(self, roman_numeral):
        arabic_sum = self.arabic + roman_numeral.arabic
        if arabic_sum > 3999:
            raise RuntimeError(
                "Sum of " + self.roman + " and " + roman_numeral.roman + " results in an invalid roman numeral")

        return RomanNumeral.from_arabic(arabic_sum)

    @staticmethod
    def get_maps():
        return {
            "I": Roman_Map("I", 1, 3),
            "IV": Roman_Map("IV", 4, 1),
            "V": Roman_Map("V", 5, 1),
            "IX": Roman_Map("IX", 9, 1),
            "X": Roman_Map("X", 10, 3),
            "XL": Roman_Map("XL", 40, 1),
            "L": Roman_Map("L", 50, 1),
            "XC": Roman_Map("XC", 90, 1),
            "C": Roman_Map("C", 100, 3),
            "CD": Roman_Map("CD", 400, 1),
            "D": Roman_Map("D", 500, 1),
            "CM": Roman_Map("CM", 900, 1),
            "M": Roman_Map("M", 1000, 3)
        }

    @staticmethod
    def from_arabic(arabic):
        roman = RomanNumeral.convert_to_roman(arabic)
        return RomanNumeral(roman)

    @staticmethod
    def from_roman(roman):
        return RomanNumeral(roman)

    @staticmethod
    def convert_to_arabic(roman):
        roman_to_arabic_map = RomanNumeral.get_maps()
        value = 0
        index = 0
        length = len(roman)
        while index < length:
            first = roman[index]
            second = ''
            if index < length - 1:
                second = roman[index + 1]

            if first + second in roman_to_arabic_map.keys():
                value += roman_to_arabic_map[first + second].arabic
                index += 1
            else:
                value += roman_to_arabic_map[first].arabic

            index += 1

        return value

    @staticmethod
    def convert_to_roman(arabic):
        roman_to_arabic_map = RomanNumeral.get_maps()
        roman = ""
        remainder = arabic
        while remainder > 0:
            for key, roman_map in sorted(roman_to_arabic_map.items(), key=lambda(k, v): roman_to_arabic_map[k].arabic, reverse=True):
                if remainder >= roman_map.arabic:
                    remainder -= roman_map.arabic
                    roman += roman_map.symbol
                    break

        return roman

    @staticmethod
    def is_valid_roman(roman):
        roman_maps = RomanNumeral.get_maps()
        counts = {}
        length = len(roman)
        for (i, c) in enumerate(roman):
            first = c
            second = ""
            if i < length - 1:
                second += roman[i + 1]

            if first + second in roman_maps:
                if first + second not in counts:
                    counts[first + second] = 0

                counts[first + second] += 1

                if counts[first + second] > roman_maps[first + second].max:
                    return False
            else:
                if first not in counts:
                    counts[first] = 0

                counts[first] += 1

                if counts[first] > roman_maps[first].max:
                    return False

        return True
