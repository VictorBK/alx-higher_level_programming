#!/usr/bin/python3

"""Module contains a function that converts class to JSON."""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure."""
    return obj.__dict__
