#!/usr/bin/python3
import sys
from os.path import exists
from json import dumps
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if not exists("add_item.json"):
    save_to_json_file([], "add_item.json")

json_list = load_from_json_file("add_item.json")
for arg in sys.argv[1:]:
    json_list.append(arg)
save_to_json_file(json_list, "add_item.json")
