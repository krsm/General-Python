# -*- coding: utf-8 -*-
"""
Simple study related to context-manager

1. define a class with an __enter__ and __exit__ method.

2. __enter__ is the before method and can return the value you catch with the as clause

3. __exit__ is the after method and accepts three arguments (excpetion_type, execption_instance, traceback).
It can return True to  supress exceptions that occur with block.

4. __init__ shoud be used to catch arguments to your context-manager (filename to open, etc)

"""

class ContextManager(object):

    def __init__(self):
        print ("__init__")

    #before stuff
    def __enter__(self):
        print("__enter__")

    def __exit__ (self, type, value, traceback):
        print()


if __name__ == "__main__":

    pass
