original_list = [1, 2, 3, 2, 4, 5, 6, 4, 7, 8]

unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
