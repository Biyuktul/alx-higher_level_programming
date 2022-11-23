#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
    and then save them to a file:
 """
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    with open("add_item.json", "r+") as f:
        json_string = load_from_json_file("add_item.json")
        f.write(sys.argv[1:] + json_string)
else:
    with open("add_item.json", "w+") as f:
        save_to_json_file(sys.argv[1:], f)