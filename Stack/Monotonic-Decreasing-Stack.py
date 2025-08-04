def monotonicDecreasing(nums):
    stack = []
    result = []

    for num in nums:
        while stack and stack[-1] < num:
            stack.pop()
        
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        
        stack.append(num)

    return result