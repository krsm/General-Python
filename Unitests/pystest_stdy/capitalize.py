# -*- coding: utf-8 -*-
"""

Simple study related to pytest

"""


# it will receive a string and capitalize
def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string argument')
    else:
        return s.capitalize()


