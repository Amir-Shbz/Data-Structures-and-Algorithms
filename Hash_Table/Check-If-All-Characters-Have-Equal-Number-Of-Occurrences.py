# 1941
# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences 
# (i.e., the same frequency).


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s: 
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        all_vals = d.values()
        return len(set(all_vals)) == 1