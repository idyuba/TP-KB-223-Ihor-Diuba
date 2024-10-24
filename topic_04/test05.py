def add(a, b):
    return a + b

def getNumber(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f" EROR: not integer")

def getOperation():

    pass

a = getNumber("What's a: ")
b = getNumber("What's b: ")
result = add(a, b)

print(f"Result of adding {a} and {b}  = {result}")





