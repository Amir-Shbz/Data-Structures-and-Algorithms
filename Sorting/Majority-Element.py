#169
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Solution: Canceling Out

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = 0
        a = -1
        for i in nums:
            if i == a:
                c += 1
            else:
                if c == 0:
                    a = i
                    c = 1
                else:
                    c -= 1
        return a if c > 0 else -1               
