from collections import OrderedDict

"""
* counter == return how many elements has in a list
* default dict == create a key if not exist yet
* ordereddict == print the object in order was inserted 
* namedtuple
* deque

"""

o = OrderedDict()

o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')

print(o)

o.popitem() #remove the last

print(o)

o.move_to_end('Jen', last=False) #move to start
print(o)

first_element = next(iter(o)) #get first element

o.popitem(False) #remove the first element

print(o)
