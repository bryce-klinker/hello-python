from katas.roman_map import all_roman_maps


MAX_ARABIC_VALUE = 3999


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
        if arabic_sum > MAX_ARABIC_VALUE:
            raise RuntimeError(
                "Sum of " + self.roman + " and " + roman_numeral.roman + " results in an invalid roman numeral")

        return RomanNumeral.from_arabic(arabic_sum)

    @staticmethod
    def from_arabic(arabic):
        roman = RomanNumeral.convert_to_roman(arabic)
        return RomanNumeral(roman)

    @staticmethod
    def from_roman(roman):
        return RomanNumeral(roman)

    @staticmethod
    def convert_to_arabic(roman):
        maps = RomanNumeral.get_maps_in_roman(roman)
        return sum(roman_map.arabic for roman_map in maps)

    @staticmethod
    def convert_to_roman(arabic):
        roman = ""
        remainder = arabic
        while remainder > 0:
            for key, roman_map in sorted(all_roman_maps.items(), key=lambda(k, v): all_roman_maps[k].arabic, reverse=True):
                if remainder >= roman_map.arabic:
                    remainder -= roman_map.arabic
                    roman += roman_map.symbol
                    break

        return roman

    @staticmethod
    def is_valid_roman(roman):
        maps = RomanNumeral.get_maps_in_roman(roman)
        counts = {}
        for roman_map in maps:
            if roman_map.symbol not in counts:
                counts[roman_map.symbol] = 0

            counts[roman_map.symbol] += 1

            if roman_map.max < counts[roman_map.symbol]:
                return False

        return True

    @staticmethod
    def get_maps_in_roman(roman):
        roman_maps = []
        index = 0
        length = len(roman)
        while index < length:
            first = roman[index]
            second = ''
            if index < length - 1:
                second = roman[index + 1]

            if first + second in all_roman_maps.keys():
                roman_maps.append(all_roman_maps[first + second])
                index += 1
            else:
                roman_maps.append(all_roman_maps[first])

            index += 1

        return roman_maps
