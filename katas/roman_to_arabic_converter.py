roman_to_arabic_map = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10
}


def roman_to_arabic(roman):
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
