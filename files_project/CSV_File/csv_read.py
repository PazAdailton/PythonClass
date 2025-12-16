open_csv_txt = open('csv_data.txt', 'r')
read_csv = open_csv_txt.readlines()
open_csv_txt.close()


lines = [line.strip() for line in read_csv[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].title()

    print(f'{name} is {age}, studying {degree} at {university}')


sample_csv_value = ','.join(['rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)