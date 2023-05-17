# Python program to implement selection sort.
def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [5, 2, 8, 3, 1, 6, 9, 7, 4]
print("Original array:", arr)

selection_sort(arr)

print("Sorted array:", arr)