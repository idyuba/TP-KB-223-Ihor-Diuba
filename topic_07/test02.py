class Student:
    def __init__(self, name, home, mark):
        if not name:
            raise ValueError("ERROR: Empty name")
        self.name = name
        self.home = home
        self.mark = mark
    
    def __str__(self):
        return f"==[{self.name} from {self.home} with mark {self.mark}]=="

    def getScore(self):
        match self.mark:
            case "A":
                print("Your score in 90 - 100")
            case "B":
                print("Your score in 80 - 89")
            case "C":
                print("Your score in 70 - 79")
            case "D":
                print("Your score in 60 - 69")
            case "F":
                print("Your score under 59")
            case _:
                print("Wrong mark")


def get_student():
    name = input("Name: ")
    home = input("Home: ")
    mark = input("Mark: ")
    student = Student(name, home, mark)
    return student

def main():
    student = get_student()
    print(student)

    student.getScore()

main()