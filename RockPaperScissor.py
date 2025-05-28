# Problem Statement:
# You want to create a simple game of Rock-Paper-Scissors in Python that takes the input as Rock,
#  Paper, or Scissors and allows you to compete against the computer.

# Question:
# How can you create a Python program that allows the player to play Rock-Paper-Scissors against 
# the computer?

#-------------------------------------------------------------------------------------------

# Date - 28 May,2025 , Code written by Shalini Singh

# rock =0  , paper = 1 , scissor =2
# scissor can cut paper so scissor wins over paper.     2>1
# paper can cover rock so paper wins over rock          1>0
# rock can smash scissor so rock wins over scissor      0>2

import random

class game :
    def __init__(self,gameOption):
        self.gameOption = gameOption

    def findOption(self):
        match self.gameOption:
            case 0 : return( "Rock")
            case 1 : return( "Paper")
            case 2 : return( "Scissor")


try:
    # Generate random number between 0 to 2 
    computerChoice= random.randrange(0,2)
    
    # check the computer option (rock, paper,scissor)
    option1 = game(computerChoice)
    computerOption = option1.findOption()

    # Get input from user
    userChoice = int (input("Let's start Rock, Paper, Scissor game." \
    " \nPlease press 0 for Rock, 1 for paper and 2 for Scissor then press enter  : "))

    if userChoice in [0,1,2]:
        # check the user's option (rock, paper,scissor)
        option2 = game(userChoice)
        userOption = option2.findOption()
    
        print("Computer's Option : " ,computerOption)
        print("User's Option : ",userOption)

        if (userChoice == computerChoice) :
            print("It's a draw")

        elif (userChoice in [0,2]) and (computerChoice in [0,2]):
            if userChoice>computerChoice:
                print("Computer wins")
            else :
                print("User wins")

        elif (userChoice > computerChoice ):
            print("User wins")

        else :
            print("computer wins")
    
    else:
       print("Incorrect input")

except ValueError as err:
    print("Invalid input")

#---------------- End of the game code ----------------------------
