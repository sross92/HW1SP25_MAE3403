# region imports
from Die import rollFairDie as rfd, rollUnFairDie as rufd #imports functions from Die and
# renames them rfd and rufd for this problem
# endregion
# collobrated with Chat to verify the i and score statements
# region function declarations
def main():
    """
    This function rolls a fair die 1000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores =[0] * 6   # create a list with 6 elements/items initialized to 0's
    n =1000   # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rfd()  # score = 1 to 6
        scores[score -1] += 1  # increment score-1 item b/c 0 indexing start
    # print the result
    print("After rolling the die 1,000 times:")
    for i, count in enumerate(scores):
        print(f"Probablility of rolling a {i+1}: {count/ n:.4f}")

# endregion
def main2():
    """
    This function rolls a fair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0] * 6  # create a list with 6 elements/items initialized to 0's
    n = 10000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rfd()  # score = 1 to 6
        scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start
    # print the result
    print("After rolling the die 10,000 times:")
    for i, count in enumerate(scores):
        print(f"Probablility of rolling a {i + 1}: {count / n:.4f}")



def main3():
    """
    This function rolls an unfair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0] * 6  # create a list with 6 elements/items initialized to 0's
    n = 10000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rufd()  # score = 1 to 6
        scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start
    # print the result
    print("After rolling the unfair die 10,000 times:")
    for i, count in enumerate(scores):
        print(f"Probablility of rolling a {i + 1}: {count / n:.4f}")



# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()
    main3()
