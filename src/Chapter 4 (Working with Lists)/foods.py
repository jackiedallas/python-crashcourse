# create a list of your favorite food
my_foods = ['chicken', 'yogurt', 'mango', 'coffee']

# create a copy of your food for your friend
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('steak')
print(f"\nMy favorites are:\n{my_foods}")

friend_foods.append('lamb')
print(f"\nMy friend's favorites are:\n{friend_foods}")

for my_food in my_foods:
    print(f"\nI love {my_food.title()}.")

for friend_food in friend_foods:
    print(f"\nMy friend loves {friend_food.title()}.")
