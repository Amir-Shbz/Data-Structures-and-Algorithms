# 3174
# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

# Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

class Solution:
    def clearDigits(self, s: str) -> str:

        # counter = 0
        # for i in s:
        #     if i in ('1','2','3','4','5','6','7','8','9','0'):
        #         counter += 1

        # while counter != 0:
        #     s = list(s)
        #     for j in range(len(s)):
        #         if s[j] in ('1','2','3','4','5','6','7','8','9','0'):
        #             s[j] = ''
        #             s[j-1] = ''
        #             break
            
        #     s = ''.join(s)
        #     counter -= 1     
        
        # Using Stack

        stack = []
        s = list(s)
        for i in s:
            if i.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(i)       

        return ''.join(stack)    