def find_indices(arr, target):
    indices = []

    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)

    return indices

# Example usage:
array = [1, 2, 3, 4, 2, 5, 2, 6]
target_number = 2

result_indices = find_indices(array, target_number)
print(result_indices)
