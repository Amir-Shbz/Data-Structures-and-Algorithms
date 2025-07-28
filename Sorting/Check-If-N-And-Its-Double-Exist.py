# 1346

# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        arrset = set(arr)
        for i in arr:
            if 2*i in arrset and i != 0:
                return True
        cnt = 0
        for i in arr:
            if i == 0:
                cnt += 1
        if cnt < 2:
            return False                            
        return True  