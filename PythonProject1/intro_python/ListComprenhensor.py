friends_age = [15, 20, 30, 18]
age_friends = [f"My friends are {age} years old." for age in friends_age]
print(age_friends)

names = ["RolF", "BoB", "JeN"]
lower = [name.lower() for name in names]
print(lower)
names = ["rolf", "bob", "jen"]
lower = [name.upper() for name in names]
print(lower)

friend = input("Enter your name: ")
friends_name2 = ["Rolf", "bob", "Jen"]
friends_lower = [name.lower() for name in friends_name2]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")

# title transforma as palavras no padrão 1º letra Maiúscula 2º Minúscula

numbers = [0,1,2,3,4]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append((number * 2))

print(doubled_numbers)

doubled_numbers2 = [number * 2 for number in numbers]
print(doubled_numbers2)

doubled_numbers3 = [number * 2 for number in range(10)]
print(doubled_numbers3)