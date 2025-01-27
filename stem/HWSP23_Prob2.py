#region imports
from sympy.stats.rv import probability

from Dice import rollDice, rollUnFairDice  #imports functions from stem Dice
#endregion

#region functions
def main():  # main function to roll nDice fair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice =4  # number of dice
    nMinScore = nDice # total score if each die scores 1
    nMaxScore = nDice * 6  # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1   # number of possible scores
    nTally = [0] * nNumScores  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000  # how many times to roll the dice
    for i in range(nRolls):  # each loop rolls dice and increments a score
        score = rollDice(N=nDice)  # call with N=nDice
        nTally[score - nMinScore] += 1  # increment score-nMinScore item b/c 0 indexing start
    print("After {} rolls of {} dice...".format(nRolls, nDice))
    for i in range(nNumScores):  # print the fraction of rolls for each score
        score = i + nMinScore
        probability = nTally[i] / nRolls
    print(f"Probability of rolling a {score}: {probability:.4f}")



def main2():  # main function to roll nDice unfair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice = 5  # number of dice
    nMinScore = nDice  # total score if each die scores 1
    nMaxScore = nDice * 6  # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1   # number of possible scores
    nTally = [0] * nNumScores   # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000  # how many times to roll the dice
    for i in range(nRolls):  # each loop rolls dice and increments a score
        score = rollUnFairDice(N=nDice) # call with N=nDice
        nTally[score - nMinScore]  +=1   # increment score-nMinScore item b/c 0 indexing start
    print("After {} rolls of {} dice...".format(nRolls, nDice))
    for i in range(nNumScores):  # print the fraction of rolls for each score
        score = i + nMinScore
        probability = nTally[i] / nRolls
        print(f"Probability of rolling a {score}: {probability:.4f}")
#endregion

#this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()