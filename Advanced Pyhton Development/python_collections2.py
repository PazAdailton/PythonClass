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

o.popitem()

print(o)