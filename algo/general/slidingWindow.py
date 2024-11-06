###################################################
# USED FOR - MAX SUM, MIN SUM, NUMBER OF TIMES, ETC
# O (N) TC
# arr is values, k is the window size for sum (continguous)
def max_sum(arr, k): # aka sliding_window
    n = len(arr)
    if n < k:
        return -1

    currSum = sum(arr[:k]) # infinite
    maxSum = currSum

    for i in range(n - k):
        currSum = currSum - arr[i] + arr[i + k]
        maxSum = max(currSum, maxSum)

    return maxSum


arr = [16, 12, 9, 19, 11, 8]
k = 3
print("Max Sum of Window Size " + str(k) + " is:", max_sum(arr, k))
