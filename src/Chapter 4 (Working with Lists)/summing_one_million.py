# make a list of the numbers from one to one million and then use min and max to make sure your list actually starts atone and ends at one million. Also use sum to see how quickly python can ad one million numbers

# one_million = []
# for value in range(1, 1_000_001):
#     one_million.append(value)

# sum = 0  
# for num in one_million:
#     sum += num
    
# print(sum)

sum_of_million = sum(range(1, 1_000_001))
print(sum_of_million)