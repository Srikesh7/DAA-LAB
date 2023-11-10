#LEADER ARRAY
def find_leaders(arr):
    leaders = []
    max_right = float('-inf')

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            leaders.append(max_right)

    leaders.reverse()
    return leaders

# Example
arr = [16, 17, 4, 3, 5, 2]
result = find_leaders(arr)
print("Leaders in the array:", result)