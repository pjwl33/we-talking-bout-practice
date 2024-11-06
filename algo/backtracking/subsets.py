def subsets(nums):
    res = []
    # O(n * 2^n)

    # backtracking
    subset = [] # ds for the current one
    def dfs(i): # idnex of value we're making decision on
        if i >= len(nums):
            res.append(subset[:]) # copy so it isn't changed by reference
            return 

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # decision to NOT include nums[i]
        subset.pop() # remove just appended
        dfs(i + 1)
        
    dfs(0)
    # res.append(nums)
    return res