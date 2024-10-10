import math

def Merge_Sort(A, p, r):
    if p==r:
        return A
    elif p < r:
        q = math.floor((r-p)/2)

        left = Merge_Sort(A[p: q+1] , 0 , q)
        right = Merge_Sort(A[q+1: r+1] , 0 , r-q-1)

        key = max(left)
        left.append(max(right))
        right.append(key)

        result = []
        i = 0
        j = 0

        for k in range(p, r+1):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1 
               

        return result        


nums = [3, 41, 52, 26, 38, 57, 9, 49]
#nums = [4, 3, 2, 1]
result = Merge_Sort(nums, 0, len(nums)-1)

print(result)