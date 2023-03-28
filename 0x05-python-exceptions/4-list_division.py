#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            quotient = 0
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError()
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            if not isinstance(dividend, (int, float)) or not isinstance(
                divisor, (int, float)
            ):
                raise TypeError()
            quotient = dividend / divisor

        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(quotient)

    return new_list
