# Given a collection of nums, might contain duplicates, return all possible unique ones

# Backtracking still [1, 1, 2]

def permutationsTwo(nums):
    # Two lists for result and perms
    res, perm = [], []
    count = { n:0 for n in nums } # each count is 0 to start

    for n in nums:
        count[n] += 1

    # BC: perms len is == to len of nums, not more perms to check
    def dfs():
        if len(perm) == len(nums):
            res.append(perm[:])
            return
        
        for c in count:
            if count[c] > 0:
                perm.append(c)
                count[c] -= 1

                dfs()

                count[c] += 1
                perm.pop()

    dfs()
    return res
