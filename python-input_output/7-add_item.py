#!/usr/bin/python3
# script that adds all arguments to a Python list,
# and then save them to a file
"""
    script that adds all arguments to a Python list,
    and save them to a file
"""

import sys

if _name_ == "_main_":
    save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        _import_('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
"""adds all arguments to a Python list, and after that save them to a file:"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file') \
        .load_from_json_file

    try:
        loadFile = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loadFile = []

    argc = len(sys.argv)
    for idx in range(1, argc):
        loadFile.append(sys.argv[idx])
    save_to_json_file(loadFile, "add_item.json")
