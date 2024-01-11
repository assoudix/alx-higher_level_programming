#!/usr/bin/python3

def divisible_by_2(list=[]):
    """Find all even numbers in a list"""
    even = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            even.append(True)
        else:
            even.append(False)

    return (even)
