
import csv

students = []

with open("inputTest01") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name":row[0], "mark":row[1]})

for elem in sorted(students, key=lambda student: student["mark"]):
    print(f"Name is {elem['name']} Mark is {elem['mark']}")