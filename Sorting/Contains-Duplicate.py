# 217
# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set(nums)
        return len(num_set) != len(nums)