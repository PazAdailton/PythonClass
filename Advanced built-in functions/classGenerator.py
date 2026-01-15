"""
all objects that have this DUNDER NEXT METHOD
are called ITERATORS
"""
class firstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

my_gen = firstHundredGenerator()
print(next(my_gen))
print(next(my_gen))



# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop
        self.current = 2  # stop defines the range (exclusive upper bound) in which we search for the primes

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.stop:
            n = self.current
            self.current += 1

            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                return n
        raise StopIteration()


g = PrimeGenerator(15)
print(next(g))