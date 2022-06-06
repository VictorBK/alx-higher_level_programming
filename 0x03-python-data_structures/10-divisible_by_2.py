#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    value = []
    for i in my_list:
        if i % 2:
            value = value + [False]
        else:
            value = value + [True]
    return value
