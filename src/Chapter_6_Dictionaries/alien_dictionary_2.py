# make three dictionaries of aliens
alien_1 = {'color': 'green', 'points': 1}
alien_2 = {'color': 'yellow', 'points': 2}
alien_3 = {'color': 'red', 'points': 3}

# put the aliens into a list
aliens = [alien_1, alien_2, alien_3]

# loop through alien list and print each alien
for alien in aliens:
    print(alien)

# create an empty list of martians
martians = []

# make 30 martians
for martian_num in range(30):
    new_martian = {'color': 'orange', 'points': 10, 'speed': 'fast'}
    martians.append(new_martian)

for martian in martians[:5]:
    print(martian)

print("...")
print(f"A total of {len(martians)} martians were created.")
total_aliens = len(martians) + len(aliens)
print(f"Total number of aliens: {total_aliens}")

for alien in aliens:
    if alien['color'] != 'yellow':
        alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium'
    print(alien)
