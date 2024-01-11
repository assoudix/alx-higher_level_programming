#!/usr/bin/python3

def replace_in_list(my_list, ixd, element):
    """Replace identified element in a list"""
    if ixd >= 0 and ixd < len(my_list):
        my_list[ixd] = element
    return (my_list)
