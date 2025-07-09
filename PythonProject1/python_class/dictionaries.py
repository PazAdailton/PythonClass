friends_age = {"Rolf": 24, "Adm": 30, "Anne": 27}
print("friends_age :",friends_age)
friends_age["Rolf"] = 20
friends_age["Bob"] = 40
print("friends_age :",friends_age)


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]
print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

#parse tupla in dictionarie
friends2 = [("Rolf", 24), ("Bob", 30), ("Anne", 27)]
friends_age = dict(friends2)
print("friends_age :",friends_age)

