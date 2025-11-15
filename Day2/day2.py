# user_profile.py
# goal: practice input(), variables, and basic data types

# ask the user for some info
name = input("what is your name? ")
age = input("how old are you? ")
color = input("what is your favorite color? ")

# age is a string right now – let's convert it to an int
age_number = int(age)

# print a friendly summary using commas (can join different types)
print("hi,", name + "!")
print("you are", age_number, "years old.")
print("your favorite color is", color + ".")

# a concatenation example (only strings)
message = "nice to meet you, " + name + "!"
print(message)
