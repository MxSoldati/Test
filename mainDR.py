import unittest
def convert_decimal_to_roman(decimal_number):
    mult_10 = decimal_number // 10
    menor_10 = decimal_number % 10
    unidades = ''
    decenas = ''
    roman = ''
    if menor_10 < 4:
        for digit in range(menor_10):
            unidades += 'I'
    if menor_10 == 4:
        unidades += 'IV'
    if 9 > menor_10 > 4:
        unidades += 'V'
        for digit in range(menor_10):
            if digit > 4:
                unidades += 'I'
    if menor_10 == 9:
        unidades += 'IX'
    if mult_10 < 4:
        for digit in range(mult_10):
            decenas += 'X'
    if mult_10 == 4:
        decenas += 'XL'
    if 9 > mult_10 > 4:
        decenas += 'L'
        for digit in range(mult_10):
            if digit > 4:
                decenas += 'X'
    if mult_10 == 9:
        decenas = 'XC'
    roman = decenas + unidades
    return roman


