# 2.	Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.

class PairFinder:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
        
    def find_pair(self):
        # create a dictionary to store the elements and their indices
        element_dict = {}
        
        # loop through the array and check if the complement of each element exists in the dictionary
        for i, num in enumerate(self.arr):
            complement = self.target - num
            if complement in element_dict:
                # if complement exists, return the indices of the two elements
                return [element_dict[complement], i]
            else:
                # otherwise, add the element and its index to the dictionary
                element_dict[num] = i
                
        # if no pair is found, return None
        return None
# create an instance of the PairFinder class
pair_finder = PairFinder([2, 7, 11, 15], 9)

# find the pair of indices
pair_indices = pair_finder.find_pair()

# display the pair indices
print(pair_indices)