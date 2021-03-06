#!/usr/bin/env python3

"""
    Perform a checksum on a UPC
    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Natasha Gandhi, Olena Kit'
__email__ = "tash.gandhi@mail.utoronto.ca, olena.kit@mail.utoronto.ca"

# imports one per line


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    #Check type of input
    #Raise TypeError if not string
    if type(upc) != str:
        raise TypeError("Incorrect type. Input must be a string.")

    # check length of string
    # raise ValueError if not 12
    if len(upc) != 12:
        raise ValueError("Incorrect value. Input must be exactly 12 digits.")

    # convert string to array
    upc_list = list(upc)

    # convert list of strings to list of integers
    up = [int(s) for s in upc_list]

    # generate checksum using the first 11 digits provided
    generate_checksum = (10-(((up[0]+up[2]+up[4]+up[6]+up[8]+up[10])*3)+(up[1]+up[3]+up[5]+up[7]+up[9]))%10)

    # check against the the twelfth digit
    # return True if they are equal, False otherwise
    if generate_checksum == up[11]:
        return True
    else:
        return False
