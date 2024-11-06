def max_subarray(nums):
    maxSub = nums[0] # cant be 0 since have neg nums in arr
    currSum = 0

    for n in nums:
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSub = max(maxSub, currSum)

    return maxSub
