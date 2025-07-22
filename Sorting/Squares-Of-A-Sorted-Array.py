# 977

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each 
# number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # i = 0
        # k = j = len(nums)-1  
        # res = [0]*(k+1)

        # while i <= j:
        #     a = nums[i]**2
        #     b = nums[j]**2
        #     if a > b:
        #         res[k] = a
        #         i += 1
        #     else: 
        #         res[k] = b
        #         j -= 1
        #     k -= 1
        # return res             
        app = []
        for i in nums:
            app.append(i*i)
        app.sort()    
        return app    
