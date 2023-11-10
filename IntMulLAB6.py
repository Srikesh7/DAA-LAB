def multiply_without_operator(a, b):
    result = 0

    # Determine the sign of the result
    sign = -1 if (a < 0) ^ (b < 0) else 1

    # Take the absolute values for multiplication
    a, b = abs(a), abs(b)

    # Multiply using repeated addition
    for _ in range(b):
        result += a

    return sign * result

# Example usage:
num1 = 5
num2 = -3

result_multiplication = multiply_without_operator(num1, num2)
print(f"The result of {num1} * {num2} is: {result_multiplication}")
