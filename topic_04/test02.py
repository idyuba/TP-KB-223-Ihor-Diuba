# Exception

try:
    x = int(input("What's x: "))
    print(f"x  = {x}")
    y = 100 / x
    print(f"y  = {y}")
except Exception as ex:
    print(type(ex))
    print(ex.args)
    print(ex)