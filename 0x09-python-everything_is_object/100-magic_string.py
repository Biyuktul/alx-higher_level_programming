#!/usr/bin/python3
def magic_string(a=[0]):
    a[0] += 1
    return ', '.join("BestSchool" for i in range(a[0]))