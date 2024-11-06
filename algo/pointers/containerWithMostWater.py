def containerMostWater(height):
    # Brute force

    # res = 0

    # for l in range(len(height)): # left in position at least once
    #     for r in range(l + 1, len(height)):
    #         area = (r - l) * min(height[l], height[r])
    #         res = max(res, area)

    # Linear O(n) solution
    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        # elif height[l] > height[r]:
        #     r -= 1
        else:
            r -= 1  

    return res