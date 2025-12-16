# ask the user for a list of 3 friends
#for each friend we'll tell the user whether they are nearby
#for each nearby friend, well their name to `nearby_friends.txt`

friends = [f.strip() for f in input('Enter three friend names, separated by commas: ').split(',')]

people = open('people.txt', 'r')
people_nearby = [ line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

friends_nearby_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    friends_nearby_file.write(f"{friend}\n")

friends_nearby_file.close()






