
from random import randint

# creating a list of viable options that a player can use in rock, paper, scissors
options = ["rock", "paper", "scissors"]

# assigning the computer a random play
computer = options[randint(0, 2)]

player = False    #  As soon as you take your turn, your status changes from False to True because any value assigned to the variable player makes player True
player_wins = 0
computer_wins = 0

print("Welcome challenger! Today you will face off the mighty computer in an epic game of Rock, Paper, Scissors! Let's see who can get 5 wins first.")
player_consent = input("Would you like to proceed?: ")
if player_consent == "yes":
    print("Let's do this!")
else:
    exit("Okay have it your way!")

while player_wins < 5 and computer_wins < 5:
    while player == False:
        player = input("rock, paper, or scissors?: ")
        if player == computer:
            print("We have a tie!")
        elif player == "rock":
            if computer == "paper":
                computer_wins += 1
                print("Computer wins!")
            else:
                player_wins += 1
                print("Player Wins")
        elif player == "paper":
            if computer == "scissors":
                computer_wins += 1
                print("Computer wins!")
            else:
                player_wins += 1
                print("Player Wins")
        elif player == "scissors":
            if computer == "rock":
                computer_wins += 1
                print("Computer wins!")
            else:
                player_wins += 1
                print("Player Wins")
        else:
            print("Error. Try inputting a valid response. Check capitalization.")
        player = False
        computer = options[randint(0,2)]
        if player_wins == 5:
            print("The player wins!")
            break
        elif computer_wins == 5:
            print("The computer wins!")
            break


