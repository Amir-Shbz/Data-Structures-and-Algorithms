# 594

# We define a harmonious array as an array where the difference between its 
# maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious 
# subsequence among all its possible subsequences.

import collections

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        x = collections.Counter(nums)
        y = []

        for i in x:
            if x[i+1] > 0:
                y.append(x[i] + x[i+1])
            y.append(0)    

        return max(y)
            