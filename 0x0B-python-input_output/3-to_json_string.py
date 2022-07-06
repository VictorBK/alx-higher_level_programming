#!/usr/bin/python3

"""Module that defines a function that returns a json representation of an object."""
import json


def to_json_string(my_obj):
    """ ReturnJSON representation of a string object. """
    return json.dumps(my_obj)
