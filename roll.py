# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.

import random

def rollDice(numOfDice):
    playAgain = "1"
    while playAgain == "1":
        for d in range(1, numOfDice+1):  
            print(random.randint(1,6))
        print("Do you want to roll again?")
        playAgain = str(input("Please enter 1 for Yes, or anything else to end the game: "))

rollDice(3)

