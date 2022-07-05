#!/usr/bin/python3
"""
Module to define a function that appends a string to the end of a text file
"""


def append_write(filename="", text=""):
    """ Appends to the text file and returns the number of characters added """
    with open(filename, mode="a", encoding="utf=8") as f:
        return f.write(text)
