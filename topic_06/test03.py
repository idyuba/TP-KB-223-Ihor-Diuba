name = input("What's your name: ")

with open("fileName", "a") as file:
    file.write(f"{name}\n")