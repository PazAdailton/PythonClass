"""
are mutable: dictionaries, lists
not mutable: integers(all functions return new int objects), floats, strings, tuples

default values for parameters

Any argument that has default value has to follow arguments that do not have default value
"""
from email.charset import add_codec

accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str = 'checking') -> float:
    accounts[name] += amount
    return accounts[name]

balance = add_balance(500.00) #added default value in parameter str = 'checking'
print(balance)

# or

# add_balance(500.00)
# print(accounts['checking'])
