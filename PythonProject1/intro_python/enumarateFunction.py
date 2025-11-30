friends = ["Rolf", "John", "Anna"]
counter = 0
for counter, friend in enumerate(friends, start=1):
    print(counter)
    print(friend)

print(list(enumerate(friends)))
print(list(zip([0,1,2], friends)))
print(dict(enumerate(friends)))