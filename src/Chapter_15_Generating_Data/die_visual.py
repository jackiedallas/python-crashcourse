from die import Die
import plotly.express as px  # type: ignore


# create a D6.
die_1 = Die()
die_2 = Die()

# make some rolls and store the results in a list
results = []

for roll_num in range(1000):
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

print(len(frequencies))
print(frequencies)
print(f"""
Times Rolled:

2: {frequencies[0]}
3: {frequencies[1]}
4: {frequencies[2]}
5: {frequencies[3]}
6: {frequencies[4]}
7: {frequencies[5]}
8: {frequencies[6]}
9: {frequencies[7]}
10: {frequencies[8]}
11: {frequencies[9]}
12: {frequencies[10]}
""")

# visualize the results
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
