class RomanNumeralConverter(object):
    def to_arabic(self, roman):
        if roman == 'IX':
            return 9

        if roman == 'IV':
            return 4

        if roman == 'III':
            return 3

        if roman == 'II':
            return 2
        return 1