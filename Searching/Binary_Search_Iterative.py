import math

def Binary_Search(nums, value):

    start = 0
    end = len(nums)-1

    mid = -1

    for i in range(len(nums)):

        mid = math.floor((end-start+1)/2)
        if value == nums[mid]:
            return mid
        elif value > nums[mid]:
            start = mid + 1
        elif value < nums[mid]:
            end = mid - 1    

nums = [2, 3, 5, 6, 8, 9, 10]
result = Binary_Search(nums, 3)

print(result)         
