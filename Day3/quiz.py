weather = input("Is it raining? (yes/no): ")
temp = int(input("What's the temperature outside? "))

if weather == "yes" and temp < 60:
    print("Wear a coat and bring an umbrella ☂️🧥")
elif weather == "yes" and temp >= 60:
    print("Just bring an umbrella ☂️")
elif weather == "no" and temp < 50:
    print("Bundle up, it’s chilly! 🧣")
else:
    print("Perfect weather — enjoy your day! 🌞")


age = int(input("Enter your age: "))
mood = input("Do you want something funny or scary? ").lower()

if age < 13 and mood == "funny":
    print("Try 'Minions' 🍌")
elif age < 13 and mood == "scary":
    print("Try 'Goosebumps' 👻")
elif age >= 13 and mood == "funny":
    print("Try 'Mean Girls' 💅")
else:
    print("Try 'A Quiet Place' 😱")