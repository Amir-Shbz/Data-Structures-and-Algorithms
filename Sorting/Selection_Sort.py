
def Selection_Sort(nums):
    n = len(nums)
    for i in range(0, n-1):
        key = nums[i]
        min_j = i
        for j in range(i+1, n):
            if nums[j] < key:
                min_j = j
        nums[i] = nums[min_j]
        nums[min_j] = key

    return nums    

nums = [1, 2, 6, 5, 3, 10, 9]
result = Selection_Sort(nums)

print(result)