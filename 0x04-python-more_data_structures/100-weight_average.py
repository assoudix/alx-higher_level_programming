#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    n = 0
    d = 0

    for tuple in my_list:
        n += tuple[0] * tuple[1]
        d += tuple[1]

    return (n / d)
