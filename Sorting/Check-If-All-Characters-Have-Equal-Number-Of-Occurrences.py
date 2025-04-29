# 1941
# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences 
# (i.e., the same frequency).


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = list(s)
        
        if len(s) > 1:
            s.sort()
            i = 1
            while s[i-1] == s[i]:
                i += 1    
                if i > len(s)-1:
                    break
                
            k = 1
            for j in range(0,len(s)-1):
                if s[j] == s[j+1]:
                    k += 1
                if s[j] != s[j+1]:
                    if k == i:
                        k = 1
                    else:
                        return False
            if k == i:
                return True  
            return False
        return True

        
# from collections import Counter
# We Also can use Counter from Collections   

# Using Hash Map
# d = {}
# for i in s: 
#   if i in d:
#      d[i] += 1
#   else:
#      d[i] = 1
# all_vals = d.values()
# return len(set(all_vals)) == 1