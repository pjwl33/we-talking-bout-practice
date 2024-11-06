def longestSubstringNoDuplicates(str):
    # returns length of substring as int
    charSet = set()
    l, res = 0, 0

    for r in range(len(str)):
        while str[r] in charSet: # it's a duplicate, update window
            charSet.remove(str[l])
            l += 1

        charSet.add(str[r])
        res = max(res, r - l + 1) # r - l + 1 is the CURERNT WINDOW SIZE

    return res
