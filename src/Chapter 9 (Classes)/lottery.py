from random import choice


picks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')
my_ticket = (2, 4, 'B', 'C')
counter = 1
winning_ticket = ()
attempts = 0

while winning_ticket != my_ticket:
    winning_ticket = tuple(choice(picks) for _ in range(4))
    attempts += 1

print(f"Your ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {attempts} attempts to match the winning ticket!")
