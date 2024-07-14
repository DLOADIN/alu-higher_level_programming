#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []

    # Collect keys with the specified value
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    # Delete keys from the dictionary
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
