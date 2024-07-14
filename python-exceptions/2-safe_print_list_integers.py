#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    desired_number = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end="")
            desired_number += 1
        except (TypeError, ValueError):
            continue
    print()
    return desired_number
