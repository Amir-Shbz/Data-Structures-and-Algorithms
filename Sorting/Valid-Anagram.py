# 242
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s1 = list(s)
        # t1 = list(t)
        # s2 = list(s).copy()
        # for i in s2:
        #     if i in t1:
        #         t1.remove(i)
        #         s1.remove(i)
   
        # if len(t1) == len(s1) == 0:
        #     return True
        # else:
        #     return False    

        if len(s) != len(t):
            return False
        s_key = collections.Counter(s)
        t_key = collections.Counter(t)
        for key,val in s_key.items():
            if t_key[key] != val:
                return False
        return True