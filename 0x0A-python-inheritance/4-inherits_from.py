#!/usr/bin/python3
""" Program that validate if an object belongs to a sublcass """



def inherits_from(obj, a_class):
    """ check whether an object inherits from a class """
    return issubclass(type(obj), a_class) and (type(obj) != a_class)
