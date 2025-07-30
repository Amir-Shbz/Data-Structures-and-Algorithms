# 387

# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = collections.Counter(s)

        for i in s:
            if x[i] == 1:
                return s.index(i)

        return -1     