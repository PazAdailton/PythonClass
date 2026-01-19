"""
 Any() functions takes an iterable and return True or False if ANY is True
 All() returns True if ALL elements are True
"""


friends = [
    {'name': 'Rolf',
     'location': 'Washington, D.C.'
     },

    {'name': 'Anna',
     'location': 'San Francisco'
     },

    {'name': 'Charlie',
     'location': 'San Francisco'
     },

    {'name': 'Jose',
     'location': 'San Francisco'
     }
]

your_locations = input("Where are you right now? ")
friends_nearby = [friend for friend in friends if your_locations == friend['location']]

if any(friends_nearby):
    print(f"You are not alone!")

