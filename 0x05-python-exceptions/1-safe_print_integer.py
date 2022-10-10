#!/usr/bin/python3
def safe_print_integer(value):
    try:
        result = int(value)
    except (ValueError, TypeError):
        return (False)
    else:
        print("{:d}".format(result))
        return (True)
