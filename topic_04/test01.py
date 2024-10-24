
# print("Hello)

# a = 10 / 0  ZeroDivisionError: division by zero
# b = c + 7 NameError: name 'c' is not defined
# c = "a" + 7 TypeError: can only concatenate str (not "int") to str
# ValueError: invalid literal for int() with base 10: 'qw'



try:
    x = int(input("What's x: "))
    print(f"x  = {x}")
    y = 100 / x
    print(f"y  = {y}")
except ValueError:
    print(f"x is not an integer")
except ZeroDivisionError:
    print(f"x ZERO")