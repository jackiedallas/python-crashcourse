# think of five places in the world you'd like to visit, put them in a list
bucket_list = ['maldives', 'iceland', 'australia', 'antarctica', 'egypt']

# print the list in the original order
print(f"Bucket List original order:\n{bucket_list}\n")

# print the list in a sorted order without modifying the original list
print(f"Bucket List alphabetical order:\n{sorted(bucket_list)}\n")

# show that your list is still in the original order by printing it again
print(f"Bucket List back to original order:\n{bucket_list}\n")

# use reverse method to reverse the order of your original list
bucket_list.reverse()
print(f"Bucket List original order reversed:\n{bucket_list}\n")

# use the reverse method again to change the order back to the original order
bucket_list.reverse()
print(f"Bucket List back to original order after using the reverse method:\n{bucket_list}\n")

# use the sort method to change the original order to alphabetical
bucket_list.sort()
print(f"Bucket List original order changed to Alphabetical:\n{bucket_list}\n")

# use the sort method and change the original order to reverse-alphabetical
bucket_list.sort(reverse=True)
print(f"Bucket List reverse-alphabetical order:\n{bucket_list}\n")
