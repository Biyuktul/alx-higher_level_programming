#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
list_two = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
max_value = max_integer(list_two)
print("2 Max: {}".format(max_value))

my_list = [-5, -3, -8, -1, -9]
max_value = max_integer(my_list)
print("N Max: {}".format(max_value))