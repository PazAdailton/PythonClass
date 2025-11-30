class Car:
    def __init__(self, make, model ):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"Car {self.make} {self.model}"

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError("Tried to add a `{car.__clas__.__name__}` to the garage but you can only add `Car` objects")
        self.cars.append(car)


ford = Garage()
fiesta = Car("Fiesta", "Fiesta")
try:
    ford.add_car('fiesta')
except TypeError:
    print("Your car was not a Car")
except ValueError:
    print(f"Something weird happened...")
finally:
    print(f"The garage now has {len(ford)} cars.")



#raise usar raise dentro do bloco de except não precisa do tipo do error
#finally sempre será executado