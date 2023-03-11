#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        new_list = my_list.pop()
        print("{:d}".format(new_list))
