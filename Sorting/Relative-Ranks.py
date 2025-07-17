# 506

# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. 
# All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, 
# the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their 
# placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        y = score.copy()
        y.sort()
        yd = {}
        for i in range(len(score)-1,-1,-1):
            if i ==  len(score)-1:
                yd[y[i]] = "Gold Medal"
            if i ==  len(score)-2:
                yd[y[i]] = "Silver Medal"    
            if i ==  len(score)-3:
                yd[y[i]] = "ronze Medal"
            else:
                yd[y[i]] = str(len(y)-i)

        for i in range(len(score)):
            score[i] = yd[score[i]]

        return score               