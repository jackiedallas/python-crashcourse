from die import Die
import plotly.express as px  # type: ignore


# create a D6.
die_1 = Die()
die_2 = Die()

# make some rolls and store the results in a list
results = []
num_of_rolls = 145
simulation_count = 5
total_sims = num_of_rolls * simulation_count


for roll_num in range(int(total_sims)):
    rolls = die_1.roll() + die_2.roll()
    results.append(rolls)
    
# analyze the results
frequencies = []
# possible_results = range(1, die.num_sides+1)
max_results = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_results+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
title = f"Roll Results of {str(simulation_count)} Monopoly Games"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
