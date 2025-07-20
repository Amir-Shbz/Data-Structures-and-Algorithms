# 747

# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much as every other number in 
# the array. If it is, return the index of the largest element, or return -1 otherwise.

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        x = max(nums)

        for i in nums:
            if i != x and x < 2*i:
                return -1
        return nums.index(x)