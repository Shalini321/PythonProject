# Problem Statement:
# Create a game in which user guesses a random number in python.

# Questions:
# - How will generate random number and how will you set the range?
# - How to add attempts in your code, that user can have only 5 attempts to play?
# - How will you subtract a attempt when user plays it one time?
# - How will you show the ‘YOU WON!’ and ‘YOU LOST’ message?

import random

firstNumber=int(input("Enter First number : "))

secondNumber= int(input("Enter second number : "))

random_number = random.randrange(firstNumber,secondNumber)
#print (random_number)

x=1
while x<=5:
    
    checkNum= int(input("Guess the number :"))
    if(checkNum==random_number):
        print ("Correct guess, You Won!")
        break
    elif (checkNum != random_number and x == 5 ) :
        print("Sorry, You lost") 
    else: 
        print ("Try again")
    
    x+=1


