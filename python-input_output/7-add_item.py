#!/usr/bin/python3

import json
import sys
from os.path import isfile

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def adds_all_args(argv):
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
