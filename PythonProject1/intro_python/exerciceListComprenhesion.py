import  random
list = [0,1,2,4,5,6,7]


player = [
    {"name": "Rolf", "numbers": {1,2,3,4}},
    {"name": "Anna", "numbers": {5,2,3,5}},
]
for p in player:
    print(p["numbers"])