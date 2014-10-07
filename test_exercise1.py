#!/usr/bin/env python3

"""
Grade to gpa conversion
Assignment 1, Exercise 1, INF1340, Fall, 2014.
Module to test exercise1.py
"""

__author__ = 'Natasha Gandhi, Olena Kit'
__email__ = "tash.gandhi@mail.utoronto.ca, olena.kit@mail.utoronto.ca"


#import pytest
import pytest

# imports one per line
from exercise1 import grade_to_gpa


def test_letter_grade():
    """
    Letter grade inputs
    """
    assert grade_to_gpa("A+") == 4.0
    assert grade_to_gpa("A") == 4.0
    assert grade_to_gpa("A-") == 4.0
    assert grade_to_gpa("B+") == 4.0
    assert grade_to_gpa("B") == 4.0
    assert grade_to_gpa("B-") == 4.0
    assert grade_to_gpa("FZ") == 4.0
    
    with pytest.raises(ValueError):
        grade_to_gpa("q")
    with pytest.raises(ValueError):
        grade_to_gpa("z")
    with pytest.raises(ValueError):
        grade_to_gpa("Grade")


def test_percentage_grade():
    """
    Numeric grade inputs
    """
    assert grade_to_gpa(100) == 4.0
    assert grade_to_gpa(95) == 4.0
    assert grade_to_gpa(90) == 4.0
    
    assert grade_to_gpa(89) == 4.0
    assert grade_to_gpa(87) == 4.0
    assert grade_to_gpa(85) == 4.0

    assert grade_to_gpa(84) == 3.7
    assert grade_to_gpa(82) == 3.7
    assert grade_to_gpa(80) == 3.7

    assert grade_to_gpa(79) == 3.3
    assert grade_to_gpa(78) == 3.3
    assert grade_to_gpa(77) == 3.3

    assert grade_to_gpa(76) == 3.0 
    assert grade_to_gpa(74) == 3.0
    assert grade_to_gpa(73) == 3.0

    assert grade_to_gpa(72) == 2.7
    assert grade_to_gpa(71) == 2.7
    assert grade_to_gpa(70) == 2.7

    assert grade_to_gpa(69) == 0.0
    assert grade_to_gpa(37) == 0.0
    assert grade_to_gpa(0) == 0.0

    with pytest.raises(ValueError):
        grade_to_gpa(101)
    with pytest.raises(ValueError):
        grade_to_gpa(-1)
    with pytest.raises(ValueError):
        grade_to_gpa(200)


def test_float_input():
    """
    Float inputs
    """
    with pytest.raises(TypeError):
        grade_to_gpa(82.5)
    with pytest.raises(TypeError):
        grade_to_gpa(0.05)