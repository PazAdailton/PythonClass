#List Comprenhesion
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11, 10, 12]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)

#Zip Function

long_timers2 = list(zip(friends, time_since_seen, [1,2,3,4,5]))
print(long_timers2)



