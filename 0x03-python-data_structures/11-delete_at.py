#!/usr/bin/python3

def delete_at(list=[], idx=0):
    if idx >= 0 and idx < len(list):
        del list[idx]
    return (list)
