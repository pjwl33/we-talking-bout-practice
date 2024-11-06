# coins = [1, 3, 4, 5], amount = 7
def coinChange(coins, amount):
    cache = [amount + 1] * (amount + 1) # amount + 1 is the inf/max val
    cache[0] = 0 # base case
    # count = 0

    # then calc every val in cache up to amount
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                cache[a] = min(cache[a], 1 + cache[a - c])

    return cache[amount] if cache[amount] != amount + 1 else - 1 # if not the def val
