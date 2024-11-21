
with open("fileName", "r") as file:
    lines = file.readlines()


#print(lines)

for elem in sorted(lines,  reverse=False):
    print(f"{elem.rstrip()}")