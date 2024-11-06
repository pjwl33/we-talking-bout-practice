def threeSum(nums):
    res = []
    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]: # same value as before
            continue
        # two pointer solution like two sum
        l, r = i + 1, len(nums) - 1
        while l < r: #l and r can't be equal (unique)
            threeSum = n + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1 # it's too big
            elif threeSum < 0:
                l += 1 # it's too small
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res
