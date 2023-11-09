import sys


# Problem:
# 	Change-making Problem
#
# 	Given an unlimited supply of coins of given denominations,
# 	what is the minimum number of coins needed to make a change of size n?
#
# 	coins = 1, 3, 5

def minNumCoins(n, coins):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        current_min = sys.maxsize
        for coin in coins:
            if i - coin >= 0:
                current_min = min(current_min, dp[i - coin])
        dp[i] = 1 + current_min
    return dp[n]


n = 1
coins = [1, 3, 5]
print(f'The min num of coins to make a change is {minNumCoins(n, coins)}')
