
def Insertion_Sort_DD(nums):

    if len(nums) == 1:
        return nums
    
    key = nums[-1]

    nums = Insertion_Sort_DD(nums[0:-1])

    i = len(nums)-1
    nums.append(key)

    while key <= nums[i] and i >= 0:
        nums[i+1] = nums[i]
        i -= 1

    nums[i+1] = key

    return nums


nums = [6,5,4,2,2,1,0]
result = Insertion_Sort_DD(nums)

print(result)
