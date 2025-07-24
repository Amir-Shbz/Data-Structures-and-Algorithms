# 1005

# Given an integer array nums and an integer k, modify the array in the following way:

# choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times. You may choose the same index i multiple times.

# Return the largest possible sum of the array after modifying it in this way.

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        ng = 0
        for i in nums:
            if i < 0:
                ng += 1

        nums.sort()
        for i in range(min(ng, k)):
            nums[i] *= -1
        nums.sort()
        x = k-ng
        if x%2==1 and  x > 0:
            nums[0] *= -1

        return sum(nums)