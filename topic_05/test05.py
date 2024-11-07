from sys import argv

print("List of arguments = ", argv)

if (len(argv) == 3): 
    a = int(argv[1])
    b = int(argv[2])

    result = a + b

    print(f"Result of adding {a} and {b} = {result}")
else:
    print("EORROR: not anopught cnt of parameterrs")