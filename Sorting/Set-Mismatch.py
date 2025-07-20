# 645

# You have a set of integers s, which originally contains all the numbers from 1 to n. 
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

import collections

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # x = collections.Counter(nums)
        # a = b = 0
        # for i in range(1,len(nums)+1):
        #     if x[i] == 0:
        #         b = i
        #     if x[i] == 2:
        #         a = i

        # return [a,b]  
         
        n, a, b = len(nums), sum(nums), sum(set(nums))
		
        s = n*(n+1)//2
        
        return [a-b, s-b]          