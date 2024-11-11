# create a tuple (an immutable list)
dimensions = (200, 50)
# print(f"{dimensions[0]}\n{dimensions[1]}")
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

# dimensions[0] = 250
# print(dimensions[0])

dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)
