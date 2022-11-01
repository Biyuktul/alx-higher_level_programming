#!/usr/bin/python3
""" Roman to Integer test file
"""
def roman_to_int(roman_string):
    """Converts roman number to coresponding integer number"""
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman = {'I':1,'V':5,'X':10,'L':50,
             'C':100,'D':500,'M':1000}

    last_seen = "I"
    num = 0

    for numeral in roman_string[::-1]:
        if (roman[numeral] < roman[last_seen]):
            num -= roman[numeral]
        else:
            num += roman[numeral]
        last_seen = numeral

    return num


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
