def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
greet()

#case 1
def calculate_mpg():
    car = {
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fuel_consumed": 460
    }

    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles por gallon")
calculate_mpg()

#case 2
def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles por gallon")
calculate_mpg({
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
})

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 4600},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]
def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles por gallon")
for car in cars:
    calculate_mpg(car)