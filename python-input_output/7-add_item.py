#!/usr/bin/python3
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    # Collect command-line arguments
    arguments = sys.argv[1:]  # Exclude the script name
    
    # Try to load existing data from the JSON file
    try:
        my_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        my_list = []
    
    # Append arguments to the list
    my_list.extend(arguments)
    
    # Save the updated list to the JSON file
    save_to_json_file(my_list, 'add_item.json')

if __name__ == "__main__":
    main()
