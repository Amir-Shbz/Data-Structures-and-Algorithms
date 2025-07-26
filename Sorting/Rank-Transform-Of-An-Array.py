# 1331

# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        x = list(set(arr))
        x.sort()
        y = {}
        for i in range(len(x)):
            y[x[i]] = i+1

        for i in range(len(arr)):
            arr[i] = y[arr[i]]

        return arr        
