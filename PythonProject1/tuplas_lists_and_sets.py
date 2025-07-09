#Tuplas
friends = ("Rolf", "Anne")
print(friends)
friends += ("Jen",)
print("Tuplas: ", friends)

#Sets
print("\n")

arts_friends = {"Rolf", "Anne"}
print(arts_friends)
arts_friends.add("Jen")
print("Sets: ", arts_friends)

#oparations with sets
arts_friends2 = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

#difference
arts_but_not_science = arts_friends2.difference(science_friends)
print("arts_but_not_science :",arts_but_not_science)
science_but_not_art = science_friends.difference(arts_friends2)
print("science_but_not_art :",science_but_not_art)

#simetric difference
not_in_booths = arts_friends2.symmetric_difference(science_friends)
print("not_in_booths :",not_in_booths)

#intersection
art_and_science = arts_friends2.intersection(science_friends)
print("art_and_science :",art_and_science)

#union
all_friends = arts_friends2.union(science_friends)
print("all_friends :", all_friends)



