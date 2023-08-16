#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    total = 0
    roman_digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}    for roman in reversed(roman_string):
        arabic = roman_digits[roman]
        total += arabic if total < arabic * 5 else -arabic
    return (total)
