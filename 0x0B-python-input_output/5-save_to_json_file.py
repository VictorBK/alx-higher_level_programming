#!/usr/bin/python3
"""
Module contains function that writes Python obj to file using JSON represenation
"""
import json


def save_to_json_file(my_obj, filename):
    """ write object to a text file using JSON format. """
    with open(filename, "w") as f:
        json.dump(my_obj, f)


