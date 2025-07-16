# 414

# Given an integer array nums, return the third distinct maximum number in this array. 
# If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # set1 = set(nums)
        # if len(set1) < 3:
        #     return max(set1)
        # nums2 = list(set1)
        # nums2.sort()
        # return nums2[-3]

        set1 = set(nums)
        if len(set1) < 3:
            return max(set1)
        for i in range(2):
            set1.remove(max(set1))
        return max(set1)     
        