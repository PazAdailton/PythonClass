"""
Iterator is used to get the next value // __next__
Iterable is used to go over all the values of the iterator // __iter__ __getitem__ __len__ __sum__ __list__
"""
class FirstHundredIterator:
    def __init__(self):
        self.number = 0


    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1

            return  current
        else:
            raise StopIteration()


    def __iter__(self):
        return FirstHundredIterator()

my_iter = FirstHundredIterator
print(sum(my_iter()))


class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
       return self.cars[i]




for car in AnotherIterable():
    print(car)

