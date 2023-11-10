def diagonal_interchange(matrix):
    size = len(matrix)

    for i in range(size):
        # Swap left diagonal element with right diagonal element
        temp = matrix[i][i]
        matrix[i][i] = matrix[i][size - 1 - i]
        matrix[i][size - 1 - i] = temp

    return matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_matrix = diagonal_interchange(matrix)
print(result_matrix)
