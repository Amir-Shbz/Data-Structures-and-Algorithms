# 1356

# You are given an integer array arr. Sort the integers in the array in ascending order by the 
# number of 1's in their binary representation and in case of two or more integers have the same number 
# of 1's you have to sort them in ascending order.

# Return the array after sorting it.

class Solution:    
    def sortByBits(self, arr: list[int]) -> list[int]:
        # x = []
        # for i in arr:
        #     cnt = 0
        #     if i == 0:
        #         x.append((i,0))
        #         continue
        #     j = i
        #     while j//2 != 0:
        #         if j % 2 == 1:
        #             cnt += 1  
        #             j = j//2          
        #     x.append((i,cnt))
                
        # y = sorted(x, key=lambda y:(y[1], y[0]))

        # return [i[0] for i in y]

        arr.sort()
        tmp = []
        for i in range(len(arr)):
            tmp.append((arr[i],arr[i].bit_count()))

        sorted_arr = sorted(tmp, key=lambda x: x[1])

        return [i[0] for i in sorted_arr]
 