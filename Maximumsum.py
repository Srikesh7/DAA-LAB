array = [1, -2, 3, -4, 5, -3, 2, -2]

max_sum = float('-inf')
current_sum = 0

for num in array:
    current_sum = max(num, current_sum + num)
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
