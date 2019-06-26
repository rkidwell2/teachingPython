"""
Rosalind Kidwell
6/26/19

This program creates an interactive riddle for the cow game,
and is being used to demonstrate python fundamentals for high school students
"""
import random
from time import sleep

def cows():
    print('')
    myList = [[0, "? "],
              [2, "How many? "],
              [3, "How many cows? "],
              [4, "How many are there? "],
              [5, "How many cows are there? "],
              [6, "How many cows are there now? "],
              [5,"Do you know the answer? "],
              [8,"How many cows do you think there are? "],
              [8, "Do you know how many cows there are? "],
              [7, "How many cows are on the farm? "]]

    thisRound = random.choice(myList)
    answer = thisRound[0]
    question = thisRound[1]

    print("I have a farm with no cows yet...")
    sleep(1)

    possibles = ["add", "remove", "buy", "sell", "get rid of", "bring in"]
    for i in range(0, random.randint(3,7)):
        print("I", random.choice(possibles), random.randint(1,8), "cows on the farm.")
        sleep(1)
    print('')
    response = int(input(question))
     
    if response == answer:
        print("Correct!")
    
    else:
        print("Incorrect. There are", answer, "cows")

    again = input("\nWant to play again? (y/n) ")
    if again.lower() == "y":
        cows()

print("-" * 25)
print("Welcome to the cow game!")
print("-" * 25)

cows()

print("\nThanks for playing!")
