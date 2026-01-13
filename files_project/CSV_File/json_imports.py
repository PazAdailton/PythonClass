"""
json.load TRANSFORMA JSON EM OBJETO PYTHON

json.dump TRANSFORMA OBJETO PYTHON EM JSON
"""


import  json

#string to dictionary
file_json_friends = open('friends_json.txt')
read_json_friends = json.load(file_json_friends)
file_json_friends.close()


cars = [
    {"make": "ford", "model": "fiesta"},
    {"make": "ford", "model": "focus"}
]

#dictionary to string
open_friend_and_car_txt = open('friends_dict_and_car_list_file.txt', 'w')
write_car_list = json.dump(cars, open_friend_and_car_txt, indent=None)
open_friend_and_car_txt.close()


#string to dictionary
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
incorrect_string = json.loads(my_json_string)

print(incorrect_string[0]["name"])