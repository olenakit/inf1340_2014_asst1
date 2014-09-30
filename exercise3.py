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

#If player1 and player2 make the same decision, there is a tie so the function will return the integer 0.
# For example: If player1 chooses "Rock" and player2 chooses "Rock", it will be a tie and the function will return 0.
    if (player1 == player2):
        return 0

#If Player 1 wins then the function will return the integer 1.
# For example: If player1 chooses "Rock" and player2 chooses "Scissors", player1 wins and then function will return 1.
    if (player1==("Rock") and player2==("Scissors")) or (player1==("Scissors") and player2==("Paper")) or (player1==("Paper") and player2==("Rock")):
        return 1

#If Player2 wins then the function will return the integer 2.
# For example: If player1 chooses "Rock" and player2 chooses "Paper", player2 wins and then function will return 2.
    if (player1==("Rock") and player2==("Paper")) or (player1==("Paper") and player2==("Scissors")) or (player1==("Scissors") and player2==("Rock")):
        return 2

#If there is an error
    else:
        raise ValueError("Invalid name. Choose Rock, Paper, or Scissors.")


rps_results = {}
rps_results[("Rock", "Rock")] = 0
rps_results[("Rock", "Scissors")] = 1
rps_results[("Rock", "Paper")] = 2
rps_results[("Scissors", "Scissors")] = 0
rps_results[("Scissors", "Paper")] = 1
rps_results[("Scissors", "Rock")] = 2
rps_results[("Paper", "Paper")] = 0
rps_results[("Paper", "Rock")] = 1
rps_results[("Paper", "Scissors")] = 2

return decide_rps()