# -*- coding: utf-8 -*-
"""
Simple study related to context-manager

1. define a class with an __enter__ and __exit__ method.

2. __enter__ is the before method and can return the value you catch with the as clause

3. __exit__ is the after method and accepts three arguments (exception_type, exception_instance, traceback).
It can return True to  suppress exceptions that occur with block.

4. __init__ should be used to catch arguments to your context-manager (filename to open, etc)

"""

from contextlib import contextmanager

# First Example
class MyContextManager(object):

    # def print_msg(self, msg):
    #     print(msg)

    def __init__(self):
        print("__init__")

    #before stuff
    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, value, traceback):
        print(exc_type, value, traceback)



# Second Example
@contextmanager
def file_open(path, mode = 'w'):
    try:
        file_obj = open(path, mode)
        yield file_obj
    except OSError:
        print('Error')
    finally:
        print('Closing File')
        file_obj.close()


if __name__ == "__main__":

    # with MyContextManager() as test:
    #     test.print_msg("Using context manager")
    #     # raise ValueError

    with file_open('test.txt') as fo:
        fo.write('Context Managers')

    with file_open('test.txt') as fo:
        content = fo.read()

    print(content)
