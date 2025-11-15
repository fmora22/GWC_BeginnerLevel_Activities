# goal: practice elif chains and equality checks

score = int(input("enter your quiz score (0–100): "))

if score >= 90:
    print("grade: a, amazing job! 🎉")
elif score >= 80:
    print("grade: b, great work!")
elif score >= 70:
    print("grade: c, keep going, you are learning.")
elif score >= 60:
    print("grade: d, almost there, review a bit more.")
else:
    print("grade: f, athis is a chance to learn and try again.")

