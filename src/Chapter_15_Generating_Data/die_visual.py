from die import Die
import plotly.express as px  # type: ignore


# create a D6.
die_1 = Die()
die_2 = Die()

# make some rolls and store the results in a list
results = []

for roll_num in range(1000):
    rolls = die_1.roll()
    results.append(rolls)
    
# analyze the results
frequencies = []
possible_results = range(1, die.num_sides+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(f"""
Times Rolled:

1: {frequencies[0]}
2: {frequencies[1]}
3: {frequencies[2]}
4: {frequencies[3]}
5: {frequencies[4]}
6: {frequencies[5]}
""")

# visualize the results
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.show()
