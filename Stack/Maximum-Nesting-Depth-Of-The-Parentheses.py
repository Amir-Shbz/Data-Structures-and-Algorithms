# 1614

# Given a valid parentheses string s, return the nesting depth of s. 
# The nesting depth is the maximum number of nested parentheses.

class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        cnt = 0
        stack = []

        for i in s:
            if i == '(':
                cnt += 1
                mx = max(cnt, mx)
            elif i == ')':
                cnt -= 1

        return mx            