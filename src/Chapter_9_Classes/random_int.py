from random import randint
from random import choice
from faker import Faker  # type: ignore

# random_int = randint(1, 6)
# print(random_int)
print(randint(1, 10))
fake = Faker()
players = [fake.first_name().lower() for _ in range(5)]
first_up = choice(players)
print(first_up)
