def maxProductSubarray(nums):
    res = max(nums) # for if nums is len 1
    currMin, currMax = 1, 1 # for neutral value as product

    for n in nums:
        # deal with 0 as edge case
        if n == 0:
            currMin, currMax = 1, 1
            continue

        # positive n * currMax positive, then negatives, or n
        tempMax = n * currMax
        currMax = max(n * currMax, n * currMin, n)
        currMin = min(tempMax, n * currMin, n)
        res = max(res, currMax, currMin)

    return res
