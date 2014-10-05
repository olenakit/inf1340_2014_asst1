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
        ValueError if parameter is out of range or not an accepted value
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        accepted_values = ["A+", "A", "A-", "B+", "B", "B-", "FZ"]

        # check that the grade is one of the accepted values
        if grade in accepted_values:

        # assign grade to letter_grade
            letter_grade = grade

        #If grade input is a string, but not an accepted value, raise a ValueError
        else:
            raise ValueError("Incorrect value. Grade must be an accepted letter grade.")

    elif type(grade) is int:

        # check that grade is in the accepted range 0 to 100
        if 0 <= grade <= 100:

        # convert the numeric grade to a letter grade
            mark_to_letter = grade

        # assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)
            if mark_to_letter >= 90:
                letter_grade = "A+"
            elif mark_to_letter >= 85:
                letter_grade = "A"
            elif mark_to_letter >= 80:
                letter_grade = "A-"
            elif mark_to_letter >= 77:
                letter_grade = "B+"
            elif mark_to_letter >= 73:
                letter_grade = "B"
            elif mark_to_letter >= 70:
                letter_grade = "B-"
            else:
                letter_grade = "FZ"

        #If grade input is not in accepted range, raise ValueError
        else:
            raise ValueError("Incorrect value. Grade must be in the accepted range of 0 to 100.")
    else:
        # raise a TypeError exception
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

    #Return the gpa of the grade
    return gpa
