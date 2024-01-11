#!/usr/bin/python3

def element_at(my_list, id):
    """Returns an element from a list at position 'id'"""
    if id < 0 or id > (len(my_list) - 1):
        return None
    return (my_list[id])
