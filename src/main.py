import os
import sys
import random


choices = ["rock", "paper", "scissors"]
computer = None
player = None

player_score = 0
computer_score = 0


while True:
    while player not in choices:
        os.system('clear')
        print("SCORE:\n\tPlayer: " + str(player_score) +
                    "\n\tComputer: " + str(computer_score))
        player = input("\nRock, Paper or Scissors:\n").lower()
        computer = random.choice(choices)
    print("\n")
    print("player: " + player)
    print("computer: " + computer)
    print("\n")

    if player == computer:
        print("draw")
    elif player == "rock":
        if computer == "scissors":
            print("player won")
            player_score += 1
        elif computer == "paper":
            print("computer won")
            computer_score += 1
    elif player == "scissors":
        if computer == "paper":
            print("player won")
            player_score += 1
        elif computer == "rock":
            print("computer won")
            computer_score += 1
    elif player == "paper":
        if computer == "rock":
            print("player won")
            player_score += 1
        elif computer == "scissors":
            print("computer won")
            computer_score += 1

    player = None
    input()

sys.exit()
