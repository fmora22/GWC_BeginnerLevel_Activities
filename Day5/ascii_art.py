# ascii art gallery program

# dictionary storing art pieces
ascii_gallery = {
    "heart": """
     .:::.   .:::.
    :::::::.:::::::
    :::::::::::::::
    ':::::::::::::'
      ':::::::::'
        ':::::'
          ':'
    """,
    "tree": """
        /\\
       /  \\
      /++++\\
     /  ()  \\
     /______\\
       ||||
       ||||
    """,
    "cat": """
     /\\_/\\  
    ( o.o ) 
     > ^ <
    """
}

# show menu
print("Welcome to the ASCII Art Gallery!")
print("Choose from:", ", ".join(ascii_gallery.keys()))

choice = input("Enter your choice: ").lower()

# show the selected art
if choice in ascii_gallery:
    print("\nHere’s your art:")
    print(ascii_gallery[choice])
    
    save = input("Would you like to save this art? (yes/no): ").lower()
    if save == "yes":
        with open("my_gallery.txt", "a") as file:
            file.write(f"{choice}:\n{ascii_gallery[choice]}\n\n")
        print("Saved to my_gallery.txt ✅")
else:
    print("Sorry, that art is not in the gallery.")