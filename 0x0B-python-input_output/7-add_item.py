#!/usr/bin/python3
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_list = []
for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])
with open('add_item.json', 'w', encoding="UTF8") as file:
    json.dump(new_list, file)
