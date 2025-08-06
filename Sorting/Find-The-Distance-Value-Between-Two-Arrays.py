# 1385

# Given two integer arrays arr1 and arr2, and the integer d, 
# return the distance value between the two arrays.

# The distance value is defined as the number of elements arr1[i] such that there is not any 
# element arr2[j] where |arr1[i]-arr2[j]| <= d.

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        set2 = set(arr2)

        dset = set([i for i in range(-d, d+1)])

        cnt = 0
        for i in arr1:
            cnt += 1
            for j in dset:
                if i+j in set2:
                    cnt -= 1
                    break

        return cnt        