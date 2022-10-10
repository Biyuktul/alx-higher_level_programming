#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except BaseException:
        result = None
        return None
    finally:
        if type(result) == float:
            print("Inside result: {:.01f}".format(result))
        else:
            print("Inside result: {}".format(result))
        return result
