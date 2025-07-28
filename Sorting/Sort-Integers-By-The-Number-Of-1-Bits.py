# 1356

# You are given an integer array arr. Sort the integers in the array in ascending order by the 
# number of 1's in their binary representation and in case of two or more integers have the same number 
# of 1's you have to sort them in ascending order.

# Return the array after sorting it.

class Solution:    
    def sortByBits(self, arr: list[int]) -> list[int]:
        x = []
        for i in arr:
            cnt = 0
            if i == 0:
                x.append((i,0))
            else:
                while True:
                    if i//2 == 0:
                        break
                    elif i % 2 == 1:
                        cnt += 1
                x.append((i,cnt))

        return sorted(x, key=lambda y:(y[1], y[0]))
 