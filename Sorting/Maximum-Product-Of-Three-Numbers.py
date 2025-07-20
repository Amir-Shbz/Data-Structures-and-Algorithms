# 628

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        neg = 0
        for i in nums:
            if i < 0:
                neg += 1
        if neg <= 1:
            return nums[-1] * nums[-2] * nums[-3]
        else:
            x = nums[-1] * nums[0] * nums[1]
            y = nums[-1] * nums[-2] * nums[-3]

            return max(x,y)