# you can add elements to a list using the append (append adds elements to the end of the list) method
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
# print(motorcycles)
motorcycles.append('kawasaki')
print(f"Here is the orginal order:\n{motorcycles}\n")
motorcycles.sort() # use the sort method to rearrange the list to alphabetical order
print(f"Here is the alphabetical order:\n{motorcycles}\n")
motorcycles.sort(reverse=True) # pass the 'reverse=True' argument to reverse the alphabetical order
print(f"Here is the reversed alphabetical order:\n{motorcycles}\n")

# you can insert elements to specific indexes using teh insert method, add 'ducati' to the beginning of the list
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# you can remove elements from a list using the 'del' statement. Remove kawasaki from the list
# del motorcycles[-1]
# print(motorcycles)

# you can use the pop method to remove the last element from a list, while also being able to work with that item after removing it. 
# popped_motorcycle = motorcycles.pop()
# last_owned = motorcycles.pop()
# print(motorcycles)
# print(f"The last motorcyle I owned was a {last_owned.title()}")

# you can also specify which element of a list you want to use the pop method on
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}")

# sometimes you won't know the position of an element, but you'll know the name. You can remove an element by using it's name
# motorcycles.remove('honda')
# print(motorcycles)

# you can also work with a removed element
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"{too_expensive.title()} motorcycles are too expensive for me.")

guest_list = ['drake', 'kobe', 'wayne']
owl = guest_list[0].title()
athlete = guest_list[1].title()
goat_rapper = guest_list[2].title()
print(f"{guest_list}\n")

invitation = "you are invited to my dinner"
not_available = "isn't available for the dinner"

print(f"{owl} {invitation}.")
print(f"{athlete} {invitation}.")
print(f"{goat_rapper} {invitation}.\n")

print(f"{athlete} {not_available}")
unavailable = guest_list.remove('kobe')
print(f"{guest_list}")

genius = 'kanye'
guest_list.insert(1, genius)
goat_producer = guest_list[1].title()
print(f"{guest_list}\n")

print(f"{goat_producer} {invitation}.")
print(f"{owl} {invitation}.")
print(f"{goat_rapper} {invitation}.")
print("I found a bigger table")

guest_list.insert(0, 'mj')
guest_list.insert(2, 'hov')
guest_list.append('youngboy')

mike = guest_list[0].upper()
jay = guest_list[2].title()
yb = guest_list[-1].title()
print(f"\n{mike} {invitation}.")
print(f"{jay} {invitation}.")
print(f"{yb} {invitation}.")
print(f"{guest_list}\n")

popped_guest = guest_list.pop()
uninvite = f"Unfortunately I now only have two seats availabe for my dinner, sorry {popped_guest.title()} you can't come."
print(uninvite)
print(f"{guest_list}\n")

popped_guest = guest_list.pop()
uninvite = f"Unfortunately I now only have two seats availabe for my dinner, sorry {popped_guest.title()} you can't come."
print(uninvite)
print(f"{guest_list}\n")

popped_guest = guest_list.pop()
uninvite = f"Unfortunately I now only have two seats availabe for my dinner, sorry {popped_guest.title()} you can't come."
print(uninvite)
print(f"{guest_list}\n")

popped_guest = guest_list.pop()
uninvite = f"Unfortunately I now only have two seats availabe for my dinner, sorry {popped_guest.title()} you can't come."
print(uninvite)
print(f"{guest_list}\n")

remaining_guest = guest_list
print(f"{remaining_guest[0].title()} {invitation}.")
print(f"{remaining_guest[-1].title()} {invitation}.")

del remaining_guest[0]
del remaining_guest[-1]

print(remaining_guest)