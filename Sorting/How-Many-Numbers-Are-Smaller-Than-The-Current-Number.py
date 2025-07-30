# 1365

# Given the array nums, for each nums[i] find out how many numbers in the array are 
# smaller than it. That is, for each nums[i] you have to count the number of valid j's 
# such that j != i and nums[j] < nums[i].

# Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        x = nums.copy()
        y = {}
        x.sort()
        z = set()

        for i in range(len(x)):
            if x[i] not in z: 
                y[x[i]] = i
                z.add(x[i])    
            

        for i in range(len(nums)):
            nums[i] = y[nums[i]]

        return nums