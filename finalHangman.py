import turtle
from time import sleep
import random

wordList = ["cow", "computers", "modernity", "boop", "doggy", "cat"]

def startup():
    t = turtle.Turtle()
    t.pu()
    t.setx(-250)
    t.sety(80)
    t.pd()
    t.speed(50)
    t.fd(100)
    t.rt(180)
    t.fd(50)
    t.rt(90)
    t.fd(170)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.ht()

    print("-"*26)
    print("Welcome to HANGMAN!")
    print("-"*26)
    hangman(t)


def hangman(t):
    print("Start guessing...")
    sleep(0.5)
    word = random.choice(wordList)
    myWord = []
    for i in word:
        myWord.append(i)


    guessedLetters = [' ', ' ']
    
    hiddenWord = []
    for i in range(0, len(word)):
        hiddenWord.append("*")
    
    incorrect=0
    
    print("".join(hiddenWord))
    print("\n")
        
    while True:
        alreadyGuess = False
        guess = input("\nEnter a guess: ")
        for i in range(0,len(guessedLetters)): #checks if the letter has already been guessed
            if guessedLetters[i] == guess:
                print ("You've already guessed this letter! Try again")
                print ("".join(hiddenWord)) #word is outputted as a string
                alreadyGuess = True
                break
            else:
                guessedLetters.append(guess)
        if alreadyGuess == True:
            continue
        for i in range(0,len(myWord)):
            if guess == myWord[i]:
                hiddenWord[i] = myWord[i]
            
        if guess not in word:
            incorrect+=1
            drawHangman(t,incorrect) #the function is called to draw a piece on the hangman
            print("Letter not found.")
           
        if myWord == hiddenWord:
            print("\nYou won the game!")
            print(word)
            break
        if incorrect == 6: #ends the game if the user makes 6 incorrect guesses
            print ("\nYou guessed 6 wrong! GAME OVER")
            break
        print("".join(hiddenWord))
        
    endGame(t)


def drawHangman(t, incorrect):
    if incorrect == 1:
        t.pu()
        t.setx(-120)
        t.sety(180)
        t.pd()
        t.circle(20)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 2:
        t.pu()
        t.setx(-100)
        t.sety(160)
        t.pd()
        t.fd(50)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 3:
        t.rt(45)
        t.fd(30)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 4:
        t.pu()
        t.rt(-90)
        t.setx(-100)
        t.sety(110)
        t.pd()
        t.fd(30)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 5:
        t.pu()
        t.rt(-45)
        t.setx(-100)
        t.sety(135)
        t.pd()
        t.fd(30)
        t.ht() #hides the turtle to remove the arrow that is displayed on screen
    elif incorrect == 6:
        t.pu()
        t.rt(180)
        t.setx(-100)
        t.sety(135)
        t.pd()
        t.fd(30)
        t.pu()
        t.ht() #hides the turtle to remove the arrow that is displayed on screen

def endGame(t):
    again = input("\nPress Y if you want to play again. Press N if you're done. ")
    if again.lower() == "y":
        t.clear()
        print("Loading new game...\n")
        sleep(.5)
        startup()
    else:
        return


startup()

print("Thanks for playing!")
