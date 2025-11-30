class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name,school)
        self.salary = salary

    @property #usar esse decorador apenas em funções que retornam valores do objeto
    def weekly(self):
        return self.salary * 37.5



rolf = WorkingStudent("Rolf", "USP", 15.50)
rolf.marks.append(57)
#rolf.marks.append(99)
print(rolf.salary)
print(rolf.average())
print(rolf.weekly)