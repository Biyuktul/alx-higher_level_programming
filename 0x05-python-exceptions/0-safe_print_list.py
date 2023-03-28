#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0
    for i in range(x):
        try:
            print(f"{int(my_list[i])}", end="")
            nb_print += 1
        except ValueError as e:
            print(e)
        except IndexError:
            pass
    print()
    return nb_print
