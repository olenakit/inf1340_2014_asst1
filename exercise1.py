#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Natasha Gandhi, Olena Kit'
__email__ = "natasha's email, olena.kit@mail.utoronto.ca"

__copyright__ = "2014 Natasha Gandhi and Olena Kit"
__license__ = "MIT License"

__status__ = "Prototype"

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

    letter_grade = "letter_to_gpa"
    gpa = 0.0

   if type(grade) is 'A':
       print ("GPA is 3")
   If type(grade) is  range (80,89):
        print ("GPA is 3")

    if type(grade) is str:
        print ("letter") # remove this line once the code is implemented
        # check that the grade is one of the accepted values -- a to f
        # assign grade to letter_grade
    elif type(grade) is int:
        print("mark") # remove this line once the code is implemented
        # check that grade is in the accepted range 0 to 100
        # convert the numeric grade to a letter grade  -- specify numbers 40=F
        # assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)
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
        gpa == 3.0
    if letter_grade == "B-":
        gpa = 2.7
    if letter_grade == "FZ":
        gpa = 0.0

    return gpa

print(grade_to_gpa("A"))




