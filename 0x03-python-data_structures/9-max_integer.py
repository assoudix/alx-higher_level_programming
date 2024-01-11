#!/usr/bin/python3

def max_integer(list=[]):
    """find the biggest integer of a list"""
    if len(list) == 0:
        return (None)

    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]

    return (max)
