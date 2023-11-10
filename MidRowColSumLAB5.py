def middle_row_and_column_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])

    middle_row = rows // 2
    middle_col = cols // 2

    row_sum = sum(matrix[middle_row])
    col_sum = sum(row[middle_col] for row in matrix)

    return row_sum, col_sum

# Example usage:
matrix_to_sum = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_row_sum, result_col_sum = middle_row_and_column_sum(matrix_to_sum)
print(f"The sum of the middle row is: {result_row_sum}")
print(f"The sum of the middle column is: {result_col_sum}")
