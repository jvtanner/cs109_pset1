# Name: Joshua Tanner

"""
*************** IMPORTANT ***************
Do NOT rename this file.
Do NOT rename the q16 function or alter its
parameters in any way.

The autograder expects the following:
- Your file should be named cs109_pset1.py
- Your function should be named q16, and it
  should take 2 arguments as indicated in the
  provided starter code
- q16 must return a float
*************** IMPORTANT ***************
"""

# Do NOT add any import statements
import numpy as np

# Instructions:
# Fill in the following function.
# We will be testing your code by setting several random seeds.
# DO NOT ALTER THIS FUNCTION OUTSIDE THE BEGIN/END CODE MARKERS.
# You may add other helper functions if you wish.


def q16(seed: int = 37, ntrials: int = 100000) -> float:
    """
    Plays a game described in q16 ntrials times with a predetermined seed.
    :param seed: seed for the numpy random number generator.
    :param ntrials: the number of trials to run.
    :return: the probability as described in the written pset.
    """
    np.random.seed(seed)
    #################### BEGIN CODE ####################
    # You MUST use the function np.random.randint from numpy
    # to generate random numbers, NOT random.randint or
    # any other package.
    total = 0
    player1 = 0
    player2 = 0
    random = 0
    count1 = 0
    count2 = 1
    for x in range(ntrials):
        if total > ((2 * count1) + 1) * 100:
            player1 += random
            count1 += 1
        if total > (2 * count2) * 100:
            player2 += random
            count2 += 1
        random = np.random.randint(1, 101)
        total += random
    return player2 / (player2 + player1)

    ####################  END CODE  ####################
