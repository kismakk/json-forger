#!/usr/bin/env python3

import os
import argparse
import time
import json

WORKING_DIRECTORY = os.path.dirname(__file__)

def build_json_elements(index):
    """
    Build a dictionary representing a JSON element.

    Parameters:
        index (int): The index of the element.

    Returns:
        dict: A dictionary containing the index, name, and timestamp of the element.
    """
    return {
        "index": index,
        "name": "name_" + str(index),
        "timestamp": time.time()
    }


def create_file(args):
    """
    Create a JSON file with the given file name and number of elements.

    Args:
        args (Namespace): The command line arguments containing the file name and number of elements.

    Raises:
        SystemExit: If the file already exists in the working directory.
        SystemExit: If the number of elements is less than or equal to 0.
    """
    file_name, elements = args.file, args.elements
    
    if ".json" not in file_name:
        file_name = file_name + ".json"
    
    if os.path.exists(os.path.join(WORKING_DIRECTORY, file_name)):
        raise SystemExit(f"File {file_name} already exists.")
    
    if elements <= 0:
        raise SystemExit("Number of elements must be bigger than 0.")
    
    objects_list = []
    for element in range(0, elements):
        objects_list.append(build_json_elements(element))
    
    with open(file_name, "w") as outfile:
        json_to_file = json.dumps(objects_list, indent=4)
        outfile.write(json_to_file)
        print(f"File {file_name} created successfully to {WORKING_DIRECTORY}.")
            
    
def modify_file(args):
    """
    Modifies a JSON file by updating the value of the 'name' field at the specified index.
    Args:
        args (Namespace): Command-line arguments containing the file name, index, and the new name value.
    Raises:
        SystemExit: If the 'name' argument is not provided in the correct format.
        SystemExit: If the specified file does not exist.
        SystemExit: If the specified index is out of range in the JSON file.
    """
    file_name, index = args.file, args.index
    
    try:
        name = args.name.split("=")[1]
    except IndexError as ie:
        print(ie)
        raise SystemExit("Provide name by typing 'name=new_value'.")
    
    if ".json" not in file_name:
        file_name = file_name + ".json"

    if not os.path.exists(os.path.join(WORKING_DIRECTORY, file_name)):
        raise SystemExit(f"File {file_name} doesn't exist.")
    
    with open(file_name, "r") as openfile:
        json_from_file = json.load(openfile)
        
    try:
        json_from_file[index]["name"] = name
    except IndexError as ie:
        print(ie)
        raise SystemExit(f"Couldn't access index {index} in file {file_name}.")
    
    with open(file_name, "w") as outfile:
        modified_json_to_file = json.dumps(json_from_file, indent=4)
        outfile.write(modified_json_to_file)
        print(f"File {file_name} modified successfully.")


def main():
    parser = argparse.ArgumentParser(description="Create or modify a JSON file in the current working directory.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Creating a 'create' parser with the arguments for file and number of elements
    create_parser = subparsers.add_parser('create', aliases=["c"], help="Create a new file")
    create_parser.add_argument("file", help="File name")
    create_parser.add_argument("elements", type=int, help="Number of elements to create")
    create_parser.set_defaults(func=create_file)

    # Creating a 'modify' parser with arguments for file name, index to modify, and the new value for name field
    modify_parser = subparsers.add_parser('modify', aliases=["m"], help="Modify and existing file")
    modify_parser.add_argument("file", help="File name")
    modify_parser.add_argument("index", type=int, help="Index of the element to modify")
    modify_parser.add_argument("name", help="New value for 'name' field")
    modify_parser.set_defaults(func=modify_file)

    args = parser.parse_args()

    if args.command:
        args.func(args)
    else:
        parser.print_help()
        

if __name__ == "__main__":
    main()
