#!/usr/bin/python3

if __name__ == "__main__":
    """Sums up all the arguments and prints output."""
    import sys

    sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
