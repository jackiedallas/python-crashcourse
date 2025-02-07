import matplotlib.pyplot as plt  # type: ignore
plt.style.available


first_five = range(1, 6)
first_five_thousand = range(1, 5001)
cubes_to_five = []
cubes_to_five_thousand = []
for _ in first_five: 
    cubes_to_five.append(_ ** 3)
    
for _ in first_five_thousand:
    cubes_to_five_thousand.append(_ ** 2)

fig, ax = plt.subplots()
# ax.plot(first_five, cubes_to_five, cubes_to_five_thousand, linewidth=3)
# ax.plot(first_five_thousand, cubes_to_five_thousand, linewidth=3)
ax.plot(first_five_thousand, cubes_to_five_thousand)
plt.style.use('seaborn-v0_8')
plt.show()
