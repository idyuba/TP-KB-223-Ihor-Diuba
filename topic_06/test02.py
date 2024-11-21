name = input("What's your name: ")

file = open("fileName", "a")
file.write(f"{name}\n")
file.close()

