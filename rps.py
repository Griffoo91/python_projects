import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

#input for player choice
print("")
playerchoice = input("Please enter...\n1 for ROCK\n2 for PAPER, or\n3 for SCISSOR\n\n")
player = int(playerchoice)

#checking the user input
if player < 1 or player > 3:
    sys.exit("The number should be either 1,2 or 3.Try again later!")

# computer choice randomly generated
computerchoice = random.choice("123")
computer = int(computerchoice)

#displaying the choices of both computer and player
print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Computer chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

#logic of the game
if player == 1 and computer == 3:
    print("you win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    print("Tie game!!")
else:
    print("Computer win")
