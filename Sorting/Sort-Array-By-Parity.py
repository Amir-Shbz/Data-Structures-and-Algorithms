# 905

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i = 0
        j = len(nums)-1

        while i < j:
            if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                key = nums[j]
                nums[j] = nums[i]
                nums[i] = key
                i += 1
                j -= 1
            elif nums[i] % 2 == 1 and nums[j] % 2 == 1:
                j -= 1
            elif nums[i] % 2 == 0 and nums[j] % 2 == 0:
                i += 1
            else:
                i += 1
                j -= 1  
        return nums            