#!/usr/bin/python3
import json
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if path.isfile(filename):
    new_list = load_from_json_file(filename)
else:
    new_list = []

for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])
save_to_json_file(new_list, filename)
