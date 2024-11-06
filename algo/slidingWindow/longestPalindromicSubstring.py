def longestPalindromicSubstring(str):
    res = ""
    resLen = 0

    def checkPalindrome(str, l, r, resLen, res):
        while l >= 0 and r < len(str) and str[l] == str[r]:
            if (r - l + 1) > resLen:
                res = str[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        return resLen, res

    for i in range(len(str)):
        # odd length
        l, r = i, i
        resLen, res = checkPalindrome(str, l, r, resLen, res)
        # even length
        l, r = i, i + 1
        resLen, res = checkPalindrome(str, l, r, resLen, res)

    return res
