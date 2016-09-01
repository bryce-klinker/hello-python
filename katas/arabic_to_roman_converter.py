arabic_to_roman_map = {
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}


def arabic_to_roman(arabic):
    roman = ""
    remainder = arabic
    while remainder > 0:
        for key in sorted(arabic_to_roman_map.keys(), reverse=True):
            if remainder >= key:
                remainder -= key
                roman += arabic_to_roman_map[key]
                break

    return roman
