#SORTING ARRAY
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_result = bubble_sort(arr.copy())
print("Sorted array using bubble sort:", sorted_result)