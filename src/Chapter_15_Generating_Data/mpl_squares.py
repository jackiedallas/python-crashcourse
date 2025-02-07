import matplotlib.pyplot as plt  # type: ignore
plt.style.available
# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery',]


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# more_values = [2, 4, 6, 8, 10]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()  # fig represents the figure, ax represents a plot
ax.plot(input_values, squares, linewidth=3)  # plot method puts the array of squares in the graph

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(labelsize=14)

plt.show()  # show method brings up the figure

# set the size of tick labels
ax.tick_params(labelsize=14)

plt.show()

