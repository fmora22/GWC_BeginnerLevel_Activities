import random

# ASCII art for each choice
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Store choices and their ASCII art in a dictionary
ascii_art = {
    "rock": rock_art,
    "paper": paper_art,
    "scissors": scissors_art
}

# Game setup
choices = ["rock", "paper", "scissors"]

user = input("Choose rock, paper, or scissors: ").lower()
while user not in choices:
    user = input("Invalid choice! Please enter rock, paper, or scissors: ").lower()

comp = random.choice(choices)

# Display choices with ASCII art
print("\nYou chose:", user)
print(ascii_art[user])

print("Computer chose:", comp)
print(ascii_art[comp])

# Game logic
if user == comp:
    print("It's a tie!")
elif (user == "rock" and comp == "scissors") or \
     (user == "paper" and comp == "rock") or \
     (user == "scissors" and comp == "paper"):
    print("You win! 🎉")
else:
    print("You lose. 😞")

# Save result to file
with open("results.txt", "a") as file:
    file.write(f"You: {user}, Computer: {comp}\n")

print("\nResult saved to results.txt 📁")