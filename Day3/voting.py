# voting_check.py
# goal: practice if / elif / else and comparison operators

age = int(input("how old are you? "))

if age >= 18:
    print("you can vote in many places! 🗳️")
elif age >= 16:
    print("you might be able to pre-register, depending on where you live.")
else:
    print("you are not old enough to vote yet, but your voice still matters.")

# todo:
# change the messages so they match your own style or location
