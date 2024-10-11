import math

# Assume that nums is Sorted ...

def Binary_Search(nums, value):

    n = len(nums)
    mid = math.floor(n/2)

    if value == nums[mid]:
        return mid
    elif value > nums[mid]:
        return Binary_Search(nums[mid+1:n], value)
    elif value < nums[mid]:
        return Binary_Search(nums[0:mid], value)     


nums = [2, 3, 5, 6, 8, 9, 10]
result = Binary_Search(nums, 3)

print(result)