def custom_sort(matrix):
    # Flatten the matrix
    flattened_matrix = [element for row in matrix for element in row]

    # Custom sorting algorithm (Bubble Sort)
    n = len(flattened_matrix)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if flattened_matrix[j] > flattened_matrix[j + 1]:
                flattened_matrix[j], flattened_matrix[j + 1] = flattened_matrix[j + 1], flattened_matrix[j]

    # Reshape the sorted elements back into a matrix
    sorted_matrix = [flattened_matrix[i:i+len(matrix[0])] for i in range(0, len(flattened_matrix), len(matrix[0]))]

    # Replace diagonals with zeros
    for i in range(len(sorted_matrix)):
        sorted_matrix[i][i] = 0
        sorted_matrix[i][len(sorted_matrix) - 1 - i] = 0

    return sorted_matrix

# Example usage:
matrix_to_sort = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]

result_matrix = custom_sort(matrix_to_sort)
print(result_matrix)
