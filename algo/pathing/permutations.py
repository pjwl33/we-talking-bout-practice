# decision tree - like DFS
# recursion
def permute(nums):
    result = []

    # base case
    if (len(nums) == 1): # only one permutation
        copied = nums[:] # so we don't modify the original list by reference
        return [copied] # return is list of list

    for i in range(len(nums)):
        n = nums.pop(0) # at the 1st value
        perms = permute(nums)

        for p in perms:
            p.append(n)
            result.append(p)

        # result.extend(perms)
        nums.append(n)

    return result
