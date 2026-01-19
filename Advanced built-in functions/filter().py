"""
Filter function has two/2 arguments
The first argument the filter function is another function and it also take an iterable
"""

def starts_with_r(friend):
    return friend.startswith('R')

friends = ["Rolf", "Jose", "Randy", "Anna", "Mary"]
start_with_r = filter(starts_with_r, friends) # arg 1: return function with True or False

print(next(start_with_r))
print(next(start_with_r))


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i

start_with_r2 = my_custom_filter(lambda friend: friend.startswith('R'), friends)
print(next(start_with_r2))
print(next(start_with_r2))


#generator comprehension
another_start_with_r = (f for f in friends if f.startswith('R'))
print(next(another_start_with_r))
print(next(another_start_with_r))


