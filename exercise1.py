#!/usr/bin/env python3

"""
Grade to gpa conversion
Assignment 1, Exercise 1, INF1340, Fall, 2014.

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Natasha Gandhi, Olena Kit'
__email__ = "tash.gandhi@mail.utoronto.ca, olena.kit@mail.utoronto.ca"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        grade = letter_grade
    elif type(grade) is int:
        if grade >= 90:
            return "A+"
        if grade >= 85:
            return "A"
        if grade >= 80:
            return "A-"
        if grade >= 77:
            return "B+"
        if grade >= 73:
            return "B"
        if grade >= 70:
            return "B-"
        if grade < 69:
            return "FZ"

        # check that grade is in the accepted range 0 to 100
        # convert the numeric grade to a letter grade
        # assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)
        else:
            raise TypeError("Invalid type passed as parameter")

    # write a long if-statement to convert letter_grade
    # assign the value to gpa

    if letter_grade == "A+":
        gpa = 4.0
    if letter_grade == "A":
        gpa = 4.0
    if letter_grade == "A-":
        gpa = 3.7
    if letter_grade == "B+":
        gpa = 3.3
    if letter_grade == "B":
        gpa = 3.0
    if letter_grade == "B-":
        gpa = 2.7
    if letter_grade == "FZ":
        gpa = 0.0

    return gpa


print(grade_to_gpa("A"))






