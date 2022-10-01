#!/usr/bin/python3
search_replace(my_list, search, replace):
    """replaces an element search from a list by replace"""
    newList = list(my_list)
    for i in range(len(newList)):
        if newList[i] == search:
            newList[i] = replace
    return (newList)
