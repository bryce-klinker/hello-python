class Roman_Map:
    def __init__(self, symbol, arabic, max):
        self.symbol = symbol
        self.max = max
        self.arabic = arabic


all_roman_maps = {
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
