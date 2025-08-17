# 1047

# You are given a string s consisting of lowercase English letters. A duplicate removal 
# consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. 
# It can be proven that the answer is unique.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in s:
            if len(stack)==0:
                stack.append(i)
            else:
                if stack[-1]==i:
                    stack.pop(-1)
                else:
                    stack.append(i)
                    
        return ''.join(stack)