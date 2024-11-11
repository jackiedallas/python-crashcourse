# to make a slice you specify the index of the first and last elements you want to work with
players = ['jackie', 'devante', 'trevon', 'tumaini', 'kristian']
print(f"{players}\n")

# print the first 3 players
print(players[0:3])

# print the middle players
print(f"\n{players[1:4]}")

# omitting the first index in a slice starts your slice at the beginning of the list
print(f"\n{players[:4]}")

# omit the second index and start your slice at the end of the list
print(f"\n{players[1:]}")

# print the last 3 names of the list
print(f"\n{players[-3:]}\n")

# loop through a slice of the first 3 players in the list
print("The first 3 players on the team are:")
for player in players[:3]:
    print(f"{player.title()}")