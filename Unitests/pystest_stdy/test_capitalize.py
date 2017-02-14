# -*- coding: utf-8 -*-
"""

Simple study related to pytest

"""

import pytest
from Unitests.pystest_stdy import capitalize


# first test
def test_capitalize_string():
    c = capitalize.capitalize_string('pytest')
    assert c == 'Pytest'


# custom exception
def test_raises_exception_string_argument():
    # pytest.raises will raise a TypeError in case
    # the argument passed is not a string
    with pytest.raises(TypeError):
        capitalize.capitalize_string(10)