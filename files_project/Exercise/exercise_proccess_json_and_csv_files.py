# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json

open_csv_file = open('csv_file.txt', 'r')
read_csv_file = open_csv_file.readlines()[1:]
open_csv_file.close()

data = []



for json_data in read_csv_file:
    club, city, country = json_data.strip().split(",")
    data.append({
        "club": club,
        "city": city,
        "country": country
    }
    )

open_json_file = open('json_file.txt', 'w')
write_json_file = json.dump(data, open_json_file)
open_json_file.close()






