"""
map == transforming values
filter = filter values

list == call dunder __repr__
"""

friends = ["Rolf", "Jose", "Randy", "Anna", "Mary"]

friends_lower = map(lambda f: f.lower(), friends)
print(next(friends_lower))
print(next(friends_lower))

friends_lower2 = [f.lower() for f in friends]
print(list(friends_lower2))

friends_lower3 = (f.lower() for f in friends)
print(next(friends_lower3))
print(next(friends_lower3))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

    def __str__(self):
        return f"User: {self.username}, password: {self.password}"

    def __repr__(self):
        return f"User: {self.username}, password: {self.password}"

users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'ran', 'password': 'hash'}
]

users_map = [User.from_dict(user) for user in users]
print(users_map)

# users_map2 = map(User.from_dict, users)
# print(list(users_map2))


def transform_obj_in_dic(user_obj):
    return [
        {'username': user.username, 'password': user.password}
        for user in users_map
    ]

print(transform_obj_in_dic(users_map))





