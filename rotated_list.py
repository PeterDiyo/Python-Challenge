'''
QUESTION:
you aere given a list of numbers , obtained by rotating a sorted list an unknown number
of times.
Write a function to determine the minimum number of times the original sorted list was rotated
to obtain the given list
Example, the list [5,6,9,0,2,3,4] was obtained by rotating the sorted list [0,2,3,4,5,6,9]
3 times.

Note: if a list of sorted numbers is rotated k times, then the smallest number in the list
      ends up at position k (counting from 0 index)
'''
#Linear_search 1
def count_rotations(nums):
    pre = 0
    for position in range(pre + 1, len(nums)):
        if nums[position] < nums[pre]:
            return position
    return 0

# Example Usage:
nums = [4, 5, 6, 7, 0, 1, 2]
result = count_rotations(nums)
print(result)


#Linear_search 2
def count_rotations_linear(nunms):
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        position += 1
    return 0    

# Example Usage:
nums = [4, 5, 6, 7, 0, 1, 2]
result = count_rotations_linear(nums)
print(result)


"""
Binary Search;
-If the middle element is smaller than it's predecessor, then it is the answer.
-However, our check is not sufficient, consider the following examples;
     [7,8,1,3,4,5,6] (answer lies to the left of the middle number)
     [1,2,3,4,5,-1,0] (answer lies to the right of the middle number)
"""
def count_rotations_binary(nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        next_mid = (mid + 1) % len(nums)  # Calculate the next position using modulo to handle circular rotation
        if nums[mid] > nums[next_mid]:
            return next_mid
        elif nums[mid] > nums[low]:
            low = mid + 1
        else:
            high = mid - 1
    return 0

#Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
result = count_rotations_binary(nums)
print (result)           
#check out leetcode question