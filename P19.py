#list slicing example
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to index 5 (exclusive)
slice_1 = my_list[2:5]
print(slice_1)  # Output: [2, 3, 4]

# Get elements from the beginning to index 5 (exclusive)
slice_2 = my_list[:5]
print(slice_2)  # Output: [0, 1, 2, 3, 4]

# Get elements from index 3 to the end
slice_3 = my_list[3:]
print(slice_3)  # Output: [3, 4, 5, 6, 7, 8, 9]

# Get every second element starting from index 1
slice_4 = my_list[1::2]
print(slice_4)  # Output: [1, 3, 5, 7, 9]

# Reverse the list
reverse_list = my_list[::-1]
print(reverse_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]