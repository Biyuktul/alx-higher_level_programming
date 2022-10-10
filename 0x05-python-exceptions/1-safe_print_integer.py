#!/usr/bin/python3
def safe_print_integer(value):
    try:
        result = int(value)
    except (ValueError, TypeError, BaseException):
        return (False)
    else:
        print("{:d}".format(result))
        return (True)
