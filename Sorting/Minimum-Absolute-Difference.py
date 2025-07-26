# 1200

# Given an array of distinct integers arr, find all pairs of elements 
# with the minimum absolute difference of any two elements.

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        x = []
        for i in range(len(arr)-1):
            x.append(arr[i+1]-arr[i])
        x.sort()
        pivot = x[0]
        result = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == pivot:
                result.append([arr[i], arr[i+1]])
        return result