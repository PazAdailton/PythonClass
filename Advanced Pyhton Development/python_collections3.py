from collections import namedtuple

"""
* counter == return how many elements has in a list
* default dict == create a key if not exist yet
* ordereddict == print the object in order was inserted 
* namedtuple = utils for read database and csv file
* deque

"""


Account = namedtuple('Account', ['name', 'balance']) #has to be the same name of the variable

account = Account('checking', 1850.90)
print(account)
print(account.balance)
print(account.name)

