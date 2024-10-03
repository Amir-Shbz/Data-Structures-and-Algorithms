
def Linear_Search(nums, value):
    index = []
    for i in range(0, len(nums)):
        if nums[i] == value:
            index.append(i)

    return index

nums = [1,2,3,4,5,6,7,88,7,8,9]
result = Linear_Search(nums, 7)

print(result)