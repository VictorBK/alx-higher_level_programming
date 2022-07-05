#!/usr/bin/python3
"""
Incorporates a function that reads and prints contents from file
"""

def read_file(filename=""):
    """ Read and print text from file """
    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            print(line, end="")
