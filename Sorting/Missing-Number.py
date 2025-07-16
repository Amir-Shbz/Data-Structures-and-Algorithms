# 268

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is 
# missing from the array.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        S = 0
        n = len(nums)
        for i in nums:
            S += i
        return (n*(n+1)/2) - S    