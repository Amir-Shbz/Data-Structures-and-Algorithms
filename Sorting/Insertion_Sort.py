
def Insertion_Sort(nums):

    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

    return nums

# CLRS Example
nums = [31, 41, 59, 26, 41, 58]
result = Insertion_Sort(nums)

print(result)