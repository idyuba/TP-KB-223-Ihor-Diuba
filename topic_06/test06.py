students = []

with open("fileName1", "r") as file:
    for line in file:
        name, mark = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["mark"] = mark
        #print(f"Name is {name} Mark is {mark}")
        students.append(student)

for elem in sorted(students, key=lambda student: student["mark"]):
    print(f"Name is {elem['name']} Mark is {elem['mark']}")
