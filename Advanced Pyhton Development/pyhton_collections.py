from collections import Counter

"""
* counter == return how many elements has in a list
* default dict
* ordereddict
* namedtuple
* deque

"""


device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])


