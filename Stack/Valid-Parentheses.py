# 20

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine 
# if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for i in s:
            if i in {'(','{', '['}:
                stck.append(i)
            elif len(stck) != 0:
                if stck[-1] == '(' and i == ')':
                    stck.pop()
                elif stck[-1] == '{' and i == '}':
                    stck.pop()
                elif stck[-1] == '[' and i == ']':
                    stck.pop()
                else: 
                    return False
            else:
                return False    
        if len(stck) != 0:
            return False
        return True                       