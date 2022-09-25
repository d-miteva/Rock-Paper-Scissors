import random
import sys
from termcolor import colored, cprint

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
counter_win = 0
counter_draw = 0
counter_lose = 0
player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

while player_move != "no":

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    answer = ""

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        cprint("You win!", "green")
        counter_win += 1
        answer = input("Type [yes] to play again or [no] to quit: ")
    elif player_move == computer_move:
        cprint("Draw!", "yellow")
        counter_draw += 1
        answer = input("Type [yes] to play again or [no] to quit: ")
    else:
        cprint("You lose!", "red")
        counter_lose += 1
        answer = input("Type [yes] to play again or [no] to quit: ")

    if answer == "no":
        cprint(f"The final result is: Wins: {counter_win}, Draws: {counter_draw}, Loses: {counter_lose}", "red")
        print("Bye, see you next time!")
        break
    else:
        player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
