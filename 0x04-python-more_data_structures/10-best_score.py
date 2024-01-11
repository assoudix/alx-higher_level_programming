#!/usr/bin/python3
def best_score(mydictionary):
    if not mydictionary:
        return (None)

    return (max(mydictionary, key=mydictionary.get))
