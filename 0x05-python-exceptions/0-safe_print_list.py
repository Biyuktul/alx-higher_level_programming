#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    i = 0
    while i < x:
        try:
            result = int(my_list[i])
        except TypeError:
            break
        except IndexError:
            break
        else:
            print("{}".format(my_list[i]), end='', sep='')
            printed += 1
            i += 1
    print()
    return (printed)
