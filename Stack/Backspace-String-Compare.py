# 844

# Given two strings s and t, return true if they are equal when both are typed into 
# empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for i in s:
            if i == '#' and stack1:
                stack1.pop()
            elif i!='#':
                stack1.append(i)

        for i in t:
            if i == '#' and stack2:
                stack2.pop()
            elif i!='#':
                stack2.append(i)            

        return stack1 == stack2