

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


x = int(input("What's x? "))

if is_even(x):
    print("Even")
else:
    print("Odd")