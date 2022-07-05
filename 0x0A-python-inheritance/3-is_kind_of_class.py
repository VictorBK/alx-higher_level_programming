#!/usr/bin/python3
""" Program that checks if a class is the same
object os inherit from """


def is_kind_of_class(obj, a_class):
    """ check if an object is an instance of a class,
        or an instance of a class that inherited from
        the specified class
    """
    return isinstance(obj, a_class)
