# 2000

# Given a 0-indexed string word and a character ch, reverse the segment of 
# word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment 
# that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x = []
        stack = []
        i = -1
        for j in word:
            stack.append(j)
            if j == ch:
                break
            i += 1        

        if i == len(word)-1: return word    

        while len(stack) > 0:
            x.append(stack.pop(-1))

        for j in range(i+2, len(word)):
            x.append(word[j])

        return ''.join(x)  