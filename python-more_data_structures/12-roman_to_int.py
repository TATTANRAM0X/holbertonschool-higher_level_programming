#!/usr/bin/python3


def roman_to_int(roman_string):
    
    if not roman_string or not isinstance(roman_string, str):
        return 0

    num = 0
    symbols = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    last_entry = 1000

    for letter in roman_string:
        digit = symbols[letter]

        num += digit

        if last_entry < digit:
            num -= 2 * last_entry

        last_entry = digit

    return (num)
