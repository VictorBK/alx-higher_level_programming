#!/usr/bin/python3
"""
Contains method is_same_class
returns True if object is exactly an instance of specified class
"""


def is_same_class(obj, a_class):
    """ check whether an object is an instance of a class """
    return type(obj) == a_class
