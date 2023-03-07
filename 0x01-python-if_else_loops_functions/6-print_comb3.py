#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == j or i > j:
            continue
        if j != 9 & i != 8:
            print("{}{}, ".format(i, j), end="")
        else:
            print("{}{}".format(i, j))
