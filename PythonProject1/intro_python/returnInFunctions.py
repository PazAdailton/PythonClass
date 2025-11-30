cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 4600},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]
def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f"{name} does {mpg} miles por gallon")

for car in cars:
    print_car_info(car)

def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y
print(divide(10,2))

def add(x, y=3):
    total = x + y
    return total

print(add(5))

print(1,2,3,4, sep=" - ")

defaulty = 3

def add(x, y=3):
    total = x + y
    return total
print(add(x=2))