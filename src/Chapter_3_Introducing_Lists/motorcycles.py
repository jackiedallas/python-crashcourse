# you can add elements to a list using the append (append adds elements to the end of the list) method
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
# print(motorcycles)
motorcycles.append('kawasaki')
print(f"Here is the original order:\n{motorcycles}\n")
motorcycles.sort() # use the sort method to rearrange the list to alphabetical order
print(f"Here is the alphabetical order:\n{motorcycles}\n")
motorcycles.sort(reverse=True) # pass the 'reverse=True' argument to reverse the alphabetical order
print(f"Here is the reversed alphabetical order:\n{motorcycles}\n")

# you can also sort a list temporarily with the sort function
print("Here is an example using the sorted function:")
print(sorted(motorcycles))
print(f"\n")

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