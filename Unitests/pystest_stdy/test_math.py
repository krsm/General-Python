# -*- coding: utf-8 -*-
"""

Simple study related to pytest

"""

from Unitests.pystest_stdy import math_file


# first test
def test_calc_sum():
    total = math_file.calc_sum(4, 6)
    assert total == 10


# second test
def test_calc_multiply():
    total = math_file.calc_sum(4, 6)
    assert total == 24

