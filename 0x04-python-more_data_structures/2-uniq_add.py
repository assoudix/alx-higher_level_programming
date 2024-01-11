#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_unique_list = set(my_list)
    num = 0

    for i in my_unique_list:
        num += i

    return (num)
