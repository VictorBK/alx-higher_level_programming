#!/usr/bin/python3
""" Program that validate if an object belongs to a sublcass """


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
