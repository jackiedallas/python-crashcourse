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
uninvited = f"Unfortunately I now only have two seats available for my dinner, sorry {popped_guest.title()} you can't come."
print(uninvited)
print(f"{guest_list}\n")

popped_guest = guest_list.pop()
uninvited = f"Unfortunately I now only have two seats available for my dinner, sorry {popped_guest.title()} you can't come."
print(uninvited)
print(f"{guest_list}\n")

popped_guest = guest_list.pop()
uninvited = f"Unfortunately I now only have two seats available for my dinner, sorry {popped_guest.title()} you can't come."
print(uninvited)
print(f"{guest_list}\n")

popped_guest = guest_list.pop()
uninvited = f"Unfortunately I now only have two seats available for my dinner, sorry {popped_guest.title()} you can't come."
print(uninvited)
print(f"{guest_list}\n")

remaining_guest = guest_list
number_of_guest = len(remaining_guest) # use the 'len' method to get the length of a list
print(f"I'm inviting {number_of_guest} people to my dinner.")
print(f"{remaining_guest[0].title()} {invitation}.")
print(f"{remaining_guest[-1].title()} {invitation}.")

del remaining_guest[0]
del remaining_guest[-1]

print(remaining_guest)