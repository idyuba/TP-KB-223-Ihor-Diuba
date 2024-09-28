
def add(a, b):
    return a + b

def rem(a, b):
    return a - b

a = int(input("What's a? "))
b = int(input("What's b? "))

op = input("What's operation [ + - * /]")

if op == "+":
    result = add(a, b)
    print(result)
elif op == "-":
    result = rem(a, b)
    print(result)

