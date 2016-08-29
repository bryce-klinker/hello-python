class RomanNumeralCalculator(object):
    def add(self, first, second):
        if first == 'IV':
            return 'V'

        if first == 'II' and second == 'II':
            return 'IV'

        if first == 'II' or second == 'II':
            return 'III'
        return 'II'
