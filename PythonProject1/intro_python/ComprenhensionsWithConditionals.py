ages = [22, 35, 27, 20, 21]
odds = [age for age in ages if age % 2 == 1]

print(odds)

friends = ["Rolf", "bob", "Ruth", "Charlie", "Jen"]
guests = ["Jose", "Bob", "Rolf", "charlie", "Michael"]

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))

present_friends1 = [
    name.title() for name in guests if name.lower() in friends_lower
]
print(present_friends1)
