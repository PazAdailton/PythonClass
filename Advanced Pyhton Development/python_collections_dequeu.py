from collections import deque


"""
* counter == return how many elements has in a list
* default dict == create a key if not exist yet
* ordereddict == print the object in order was inserted 
* namedtuple = utils for read database and csv file
* deque == add element in start and the end of a list and the same to remove 

"""

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))

friends.append('Jana') #added the final list
print(friends)

friends.appendleft('Jo') #added the start of the list
print(friends)

friends.pop() #removed the final list
print(friends)

friends.popleft() #removed the start list
print(friends)
