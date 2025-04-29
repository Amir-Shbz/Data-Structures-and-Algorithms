# 3174
# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

# Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

class Solution:
    def clearDigits(self, s: str) -> str:

        stack = []
        s = list(s)
        for i in s:
            if i.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(i)       

        return ''.join(stack)    