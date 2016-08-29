def arabic_to_roman(arabic):
    if arabic == 10:
        return 'X'

    if arabic == 9:
        return 'IX'

    if arabic == 5:
        return 'V'

    if arabic == 4:
        return 'IV'

    if arabic == 3:
        return 'III'

    if arabic == 2:
        return 'II'
    return 'I'
