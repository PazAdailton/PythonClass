from collections import Counter, defaultdict

"""
* counter == return how many elements has in a list
* default dict == create a key if not exist yet 
* ordereddict
* namedtuple
* deque

"""

# COUNTER   COUNTER   COUNTER   COUNTER
device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])


# DEFAULT DICT    DEFAULT DICT   DEFAULT DICT    DEFAULT DICT
"""
Without defaultdict(list)

if 'a' not in d:
    d['a'] = []
d['a'].append(1)

With defaultdict(list)

d = defaultdict(list)
d['a'].append(1) 

"""
#Ex 1

coworkers = [('rolf', 'MIT'), ('Jen', 'Oxford'), ('Anna', 'Cambridge'), ('Anne', 'Manchester')]

alma_matters = defaultdict(list)

for coworker, place in coworkers:
    alma_matters[coworker].append(place)

alma_matters.default_factory = None #raise key error

print(alma_matters['rolf'])
#print(alma_matters['Rolf']) raise key error

#Ex 2

my_company = 'Teclado'

coworkers2 = ['Jen', 'Li', 'Charlie', 'Rhys']
others_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company) #if any key exist the default value w'll be "Teclado"

for person, company in others_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers2[0]])
print(coworker_companies['Rolf'])








