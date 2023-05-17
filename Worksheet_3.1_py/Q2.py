# Python program to implement bubble sort.
def bubble_sort(arr):
    n = len(arr)
    
    # Loop through all elements in the array
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [5, 2, 8, 3, 1, 6, 9, 7, 4]
print("Original array:", arr)

bubble_sort(arr)

print("Sorted array:", arr)