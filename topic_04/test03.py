
try:
    x = int(input("What's x: "))
except ValueError:
    print(f"x is not integer")


a  = x + 10
print(f" A == {a}")