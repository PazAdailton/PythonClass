grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total / length
print(average)

lottery_numbers = {13, 21, 22, 5, 8}

players = [{"name": "Rolf", "numbers": {13,15,5,30}}, {"name": "Jen", "numbers": {13,21,5,31}}]
player_one = players[0]["name"]
player_two = players[1]["name"]

intersection_player_one = lottery_numbers.intersection(players[0]["numbers"])
intersection_player_two = lottery_numbers.intersection(players[1]["numbers"])

match_player_one = len(intersection_player_one)
match_player_two = len(intersection_player_two)

print(f"Player {player_one} got {len(intersection_player_one)} numbers right")
print(f"Player {player_two} got {match_player_two} numbers right")