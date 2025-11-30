from PythonProject1.intro_python.lambdaFunctions import average


def greet():
    print("Hello")

hello = greet
hello()

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
    "average": avg,
    "total": total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": {67,90,95,100}},
    {"name": "Bob", "grades": {56,78,80,90}},
    {"name": "Jen", "grades": {98,90,95,99}},
    {"name": "Anne", "grades": {100,100,95,100}}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    operations_functions = operations[operation]
    print(operations_functions(grades))