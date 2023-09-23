# Write a game that:
# • allows the user to play rock, paper,
# scissors against the computer
# • must display the computer’s choice
# and show the result of the game
import random

print("-- WELCOME TO ROCK PAPER SCISSORS --")
print("INSTRUCTIONS :\n--To play, type rock, paper or scissors --")

game_keys = ["ROCK", "PAPER", "SCISSORS"]


for game_key in game_keys:
    player1 = input("Player 1 : ")
    player1 = player1.upper()
    # print(player1)
    computer = random.choice(game_keys)
    computer = computer.upper()
    print("You : " + player1 + "\nComputer : " + computer)
            #rock
    if player1 == "ROCK" :
        if computer == game_keys[0]:
            print("\n -- It's a draw! -- \n")
        if computer == game_keys[1]:
            print("\n -- Oops!You loose -- \n")
        if computer == game_keys[2]:
            print("\n -- Hurray! You win -- \n")
            #paper
    if player1 == "PAPER" :
        if computer == game_keys[1]:
            print("\n -- It's a draw! -- \n")
        if computer == game_keys[2]:
            print("\n -- Oops!You loose -- \n")
        if computer == game_keys[0]:
            print("\n -- Hurray! You win -- \n")
            #scissors
    if player1 == "SCISSORS" :
        if computer == game_keys[2]:
            print("\n -- It's a draw! -- \n")
        if computer == game_keys[0]:
            print("\n -- Oops!You loose -- \n")
        if computer == game_keys[1]:
            print("\n -- Hurray! You win -- \n")



