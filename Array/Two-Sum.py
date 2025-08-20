# 1

# Given an array of integers nums and an integer target, return indices of the 
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not 
# use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        x = {}
        for i in range(len(nums)):
            x[nums[i]] = i

        for i in range(len(nums)):
            if target-nums[i] in x and x[target-nums[i]] != i:
                return [i,x[target-nums[i]]]
            