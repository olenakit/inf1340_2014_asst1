#!/usr/bin/env python3

"""
    Perform a checksum on a UPC
    Assignment 1, Exercise 2, INF1340 Fall 2014
    Module to test exercise2.py
"""

__author__ = 'Natasha Gandhi, Olena Kit'
__email__ = "tash.gandhi@mail.utoronto.ca, olena.kit@mail.utoronto.ca"

#Import function checksum from exercise2.py
from exercise2 import checksum

def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum("1234567890") is False
    # other tests


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
        checksum(786936224306)

    with pytest.raises(ValueError):
        checksum("1")
        checksum("1234567890")

    # other tests

# add functions for any other tests
