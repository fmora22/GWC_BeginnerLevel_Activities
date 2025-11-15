# dictionary_input.py
# goal: create and update a dictionary using user input

# starter dictionary for a simple user profile
profile = {
    "name": "",
    "age": 0,
    "favorite_color": ""
}

# fill values using input()
profile["name"] = input("what is your name? ")
profile["age"] = int(input("how old are you? "))
profile["favorite_color"] = input("what is your favorite color? ")

print("\nhere is your profile:")
print("name:", profile["name"])
print("age:", profile["age"])
print("favorite color:", profile["favorite_color"])

# let the user add one more key/value pair
new_key = input("\nadd one more detail (e.g. hobby, game, pet): ")
new_value = input("what is your " + new_key + "? ")

profile[new_key] = new_value

print("\nupdated profile dictionary:")
print(profile)

# remeber \n is for formating 