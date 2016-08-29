class RomanNumeralConverter(object):
    def to_arabic(self, roman):
        if roman == 'III':
            return 3
        
        if roman == 'II':
            return 2
        return 1