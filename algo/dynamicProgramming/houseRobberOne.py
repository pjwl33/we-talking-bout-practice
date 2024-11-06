def rob(nums) -> int:
    rob1, rob2 = 0, 0
    # for each house
    for n in nums:
        # [rob1, rob2, n, n + 1, ...]
        # always update rob1 to be rob2 can't be adj
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    
    return rob2 # equal to the last value