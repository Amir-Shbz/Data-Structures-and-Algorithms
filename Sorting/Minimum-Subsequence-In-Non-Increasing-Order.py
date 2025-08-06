# 1403

# Given the array nums, obtain a subsequence of the array whose sum of elements is 
# strictly greater than the sum of the non included elements in such subsequence. 

# If there are multiple solutions, return the subsequence with minimum size and 
# if there still exist multiple solutions, return the subsequence with the maximum total sum of all 
# its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

# Note that the solution with the given constraints is guaranteed to be unique. 
# Also return the answer sorted in non-increasing order.

class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        s = sum(nums)
        l = len(nums)

        i = 0
        while i < l:
            s2 = sum(nums[0:i+1])
            if s2 > s-s2:
                break
            i += 1
        
        return nums[0:i+1]