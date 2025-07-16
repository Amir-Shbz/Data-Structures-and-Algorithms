# 350

# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

import collections

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        res = []
        for num in c1:
            if num in c2:
                res += [num] * min(c1[num], c2[num])
        return res       