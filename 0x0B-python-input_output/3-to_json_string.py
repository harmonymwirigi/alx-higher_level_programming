#!/usr/bin/python3
# 3-to_json_string.py
import json
"""
function that returns the JSON representation of an object (string):
Args: 
   obj: object to be return to string
Return:
	string
"""
def to_json_string(my_obj):
    return json.dumps(my_obj)
