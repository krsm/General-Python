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

