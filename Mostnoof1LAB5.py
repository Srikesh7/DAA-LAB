def rows_with_most_ones(matrix):
    max_ones_count = 0
    row_with_most_ones = -1

    for i in range(len(matrix)):
        ones_count = sum(matrix[i])
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            row_with_most_ones = i

    return row_with_most_ones

# Example usage:
matrix_with_ones = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

result_row = rows_with_most_ones(matrix_with_ones)
print(f"The row with the most ones is: {result_row}")
