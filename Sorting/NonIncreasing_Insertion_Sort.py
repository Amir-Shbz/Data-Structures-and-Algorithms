
def NonInc_Insertion_Sort(nums):
    
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j] < key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key

    return nums    

nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = NonInc_Insertion_Sort(nums)

print(result)
