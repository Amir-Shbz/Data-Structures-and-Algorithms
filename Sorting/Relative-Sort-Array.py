# 1122

# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements 
# that do not appear in arr2 should be placed at the end of arr1 in ascending order.

import collections

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        arr1set = collections.Counter(arr1)
        result = []

        for i in arr2:
            result += [i]*arr1set[i]
            arr1set[i] = 0

        for i in sorted(arr1set):
            if arr1set[i] != 0:
                result += [i]*arr1set[i]

        return result            