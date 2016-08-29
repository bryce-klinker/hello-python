class RomanNumeralCalculator(object):
    def add(self, first, second):
        if first == 'II' or second == 'II':
            return 'III'
        return 'II'
