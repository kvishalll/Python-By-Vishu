# Python program to implement binary search without recursion.
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If element is present at mid
        if arr[mid] == x:
            return mid
        
        # If element is smaller than mid, search left subarray
        elif arr[mid] > x:
            right = mid - 1
        
        # If element is greater than mid, search right subarray
        else:
            left = mid + 1
    
    # If element is not present in the array
    return -1
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5

result = binary_search(arr, x)

if result == -1:
    print(f"{x} was not found in the array")
else:
    print(f"{x} was found at index {result}")