def askParameters():
    a = int(input("What's a: "))
    b = int(input("What's b: "))
    c = int(input("What's c: "))
    return a, b, c

def calcSomething(a, b, c):
    result = ((a - b) / 100) + c
    return result


param1, param2, param3 = askParameters()
result = calcSomething(param1, param2, param3)

print("Result of the operation = ", result)