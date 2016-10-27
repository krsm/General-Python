# -*- coding: utf-8 -*-
"""
simple study of closures

"""

# first example
def outer_function():

    message = "Hi"

    def inner_function():

        print(message + " from inner_function - first example")

    return inner_function()

# second example


if __name__ == "__main__":

    # run first example
    outer_function()
