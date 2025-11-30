my_student = {
    "name": "Rolf Smith",
    "grades": {70, 88, 90, 99}
}

def average_grade(student):
    return sum(my_student["grades"]) / len(my_student["grades"])

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades


    def average(self):
        return sum(self.grades) / len(self.grades)

my_student_one = Student("Rolf Smith", [70,88,90,99])
print(my_student_one.name)

print(my_student_one.average())
