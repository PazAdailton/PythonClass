"""
These are functions that accept other functions
as parameters and run them inside of their own body
"""


def greet():
    print('Hello')

def before_and_after(func):
    print('Before...')
    func()
    print('After...')

before_and_after(greet)