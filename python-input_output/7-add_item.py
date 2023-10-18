#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file"""


import json
import sys
from os.path import isfile

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def adds_all_args(argv):
    """The list must be saved as a JSON representation in a file
    named add_item.json"""

    try:
        args_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        args_list = [] + '\n'

    args_list.extend(argv)
    save_to_json_file(args_list, "add_item.json")

if __name__ == "__main__":
    argv = sys.argv[1:]

    if argv:
        adds_all_args(argv)
