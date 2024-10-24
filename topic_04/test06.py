# raise

def getPassword():
    name = input("What's your password? ")
    if name != "123ko":
        raise ValueError("ACCESS DENAID")
    return name

while True:
    try:
        inputedName = getPassword()
        print(f"Name which was inputed = {inputedName}")
        break
    except:
        print("Wrong data")