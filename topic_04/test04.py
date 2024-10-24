def add(a, b):
    return a + b

def getNumber():
    while True:
        try:
            value = int(input("What's value: "))
        except ValueError:
            print(f" EROR: not integer")
        else:
            break

    return value

a = getNumber()
b = getNumber()
result = add(a, b)

print(f"Result of adding {a} and {b}  = {result}")





