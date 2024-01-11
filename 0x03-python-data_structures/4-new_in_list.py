#!/usr/bin/python3

def new_in_list(my_list, idx, new_element):
    """Replace an identified element in a copied list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[idx] = new_element
    return (copy)
