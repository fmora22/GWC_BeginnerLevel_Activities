# goal: play rock paper scissors vs the computer and save the results

import random

choices = ["rock", "paper", "scissors"]

user = input("choose rock, paper, or scissors: ").lower()

# basic input validation
if user not in choices:
    print("that is not a valid choice.")
else:
    comp = random.choice(choices)

    print("you:", user)
    print("computer:", comp)

    if user == comp:
        result = "it's a tie!"
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        result = "you win! 🎉"
    else:
        result = "you lose. 😞"

    print(result)

    # save result to a file
    with open("results.txt", "a") as file:
        file.write(f"you: {user}, computer: {comp} -> {result}\n")

    print("result saved to results.txt 📁")

# todo:
# 1. wrap this in a loop so you can play multiple rounds
# 2. keep track of wins and losses in variables
