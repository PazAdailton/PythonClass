import  json

from CSV_File.json_imports import write_car_list

#string to dictionary
with open('friends_json.txt') as file:
    read_json_friends = json.load(file)



cars = [
    {"make": "ford", "model": "fiesta"},
    {"make": "ford", "model": "focus"}
]

#dictionary to string
with open('friends_dict_and_car_list_file.txt', 'w') as file:
    write_car_list = json.dump(cars, write_car_list, indent=None)


#string to dictionary
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
incorrect_string = json.loads(my_json_string)

print(incorrect_string[0]["name"])