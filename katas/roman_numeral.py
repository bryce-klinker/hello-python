class RomanNumeral:

    def __init__(self, roman):
        self._roman = roman

    @property
    def roman(self):
        return self._roman

    @property
    def arabic(self):
        return RomanNumeral.convert_to_arabic(self.roman)

    def add(self, roman_numeral):
        arabic_sum = self.arabic + roman_numeral.arabic
        return RomanNumeral.from_arabic(arabic_sum)

    @staticmethod
    def get_map():
        return {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10
        }

    @staticmethod
    def from_arabic(arabic):
        roman_to_arabic_map = RomanNumeral.get_map()
        roman = ""
        remainder = arabic
        while remainder > 0:
            for key, value in sorted(roman_to_arabic_map.items(), reverse=True):
                if remainder >= value:
                    remainder -= value
                    roman += key
                    break

        return RomanNumeral(roman)

    @staticmethod
    def from_roman(roman):
        return RomanNumeral(roman)

    @staticmethod
    def convert_to_arabic(roman):
        roman_to_arabic_map = RomanNumeral.get_map()
        value = 0
        index = 0
        length = len(roman)
        while index < length:
            first = roman[index]
            second = ''
            if index < length - 1:
                second = roman[index + 1]

            if first + second in roman_to_arabic_map.keys():
                value += roman_to_arabic_map[first + second]
                index += 1
            else:
                value += roman_to_arabic_map[first]

            index += 1

        return value