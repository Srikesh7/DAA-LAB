def find_triplets(arr, target_sum):
    triplets = []
    n = len(arr)
    
    # Sort the array to make it easier to find triplets
    arr.sort()

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target_sum:
                triplets.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return triplets

# Example
arr = [1, 4, 2, 8, 3, 9, 7]
target_sum = 10
result = find_triplets(arr, target_sum)

print(f"Triplets with sum {target_sum}: {result}")
