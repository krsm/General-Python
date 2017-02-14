# -*- coding: utf-8 -*-
"""

Simple study related to pytest

Use command line pytest -v to run tests

"""

from Unitests.pystest_stdy import math_file
import pytest


# first test
def test_calc_sum():
    total = math_file.calc_sum(4, 6)
    assert total == 10


# second test
def test_calc_multiply():
    total = math_file.calc_multiply(4, 6)
    assert total == 24


# third test
@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100),
                         ])
def test_calc_square(test_input, expected_output):
    result = math_file.calc_square(test_input)
    assert result == expected_output


