
accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str) -> float:
    accounts[name] += amount
    return accounts[name]

transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-13.00, 'checking'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600.50, 'savings')
]

for t in transactions:
    add_balance(amount=t[0], name=t[1])
    # or add_balance(*t)




class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'ran', 'password': 'hash'}
]

# user_object = [User(username=data['username'], password=data['password']) for data in users]
user_object = [User(**data) for data in users] #when add ** needs put in order the parameters

users = [
    ('rolf', '123'),
    ('ran', '545')
]

user_objects = [User(*data) for data in users]

