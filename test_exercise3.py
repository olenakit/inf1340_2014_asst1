#!/usr/bin/env python3

"""
    Rock, Paper, Scissors
    Assignment 1, Exercise 3, INF1340, Fall, 2014.
    Module to test exercise3.py
"""

__author__ = 'Natasha Gandhi, Olena Kit'
__email__ = "tash.gandhi@mail.utoronto.ca, olena.kit@mail.utoronto.ca"

#Import pytest
import pytest

#Input the function decide_rps from exercise3.py
from exercise3 import decide_rps


def test_rps():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Paper", "Paper") == 0

# Inputs that are incorrect format and length

    with pytest.raises(TypeError):
        decide_rps("Rock", 1)
    with pytest.raises(TypeError):
        decide_rps(200, "Paper")
    with pytest.raises(TypeError):
        decide_rps("Scissors", 5.48)
    with pytest.raises(ValueError):
        decide_rps("Rock", "Spock")
    with pytest.raises(ValueError):
        decide_rps("Lizard", "Paper")
