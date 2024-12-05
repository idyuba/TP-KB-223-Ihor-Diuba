

def get_student():
    name = input("Name: ")
    home = input("Home: ")
    return {"name": name, "home":home}

def main():
    student = get_student()
    print(f"{student['name']} from {student['home']}")


main()