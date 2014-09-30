#!/usr/bin/env python3

"""
Rock, Paper, Scissors
Assignment 1, Exercise 3, INF1340, Fall, 2014.

"""

__author__ = 'Natasha Gandhi, Olena Kit'
__email__ = "tash.gandhi@mail.utoronto.ca, olena.kit@mail.utoronto.ca"


# Rock Paper Scissor Table
# Player1   Player2     Result
# Rock      Rock        Tie
# Rock      Scissors    Player1
# Rock      Paper       Player2
# Scissors  Scissors    Tie
# Scissors  Paper       Player1
# Scissors  Rock        Player2
# Paper     Paper       Tie
# Paper     Rock        Player1
# Paper     Scissors    Player2


def decide_rps(player1, player2):

    """
    :param player1: Player1 chooses Rock, Paper, or Scissors
    :param player2: Player2 chooses Rock, Paper, or Scissors
    :return: integer: The player that wins the game (if player1 wins = 1, if player2 wins = 2, if tie = 0)
    """

    #Create dictionary of all possible Rock, Paper, Scissors results.
    # If player1 and player2 choose the same value, then it is a tie and the program will return the integer 0.
    # If Player1 wins, the program will return the integer 1.
    # If player2 wins, the program will return the integer 2.

    rps_results = {("Rock", "Rock"):0,
                   ("Rock", "Scissors"):1,
                   ("Rock", "Paper"):2,
                   ("Scissors", "Scissors"):0,
                   ("Scissors", "Paper"):1,
                   ("Scissors", "Rock"):2,
                   ("Paper", "Paper"):0,
                   ("Paper", "Rock"):1,
                   ("Paper", "Scissors"):2}

    # If a player gives the wrong type of value, there will be an error
    if player1 or player2 != "Rock" or "Scissors" or "Paper":
        raise ValueError ("Incorrect value. Player must choose Rock, Paper, or Scissors.")

    #If there is no error, then the Rock, Paper, Scissors game can be decided
    else:
        return rps_results() or decide_rps()

