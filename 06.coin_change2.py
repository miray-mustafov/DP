'''
Problen: Coin Change
Denominations: 1, 3, 5, 10
What are the number of ways to return change n by using EXACTLY t coins?

F(i,t) = f(i-1,t-1) + f(i-2,t-1) + f(i-3,t-1) + f(i-5,t-1)
'''


def coinChangeExactlyTCoins(n, t, coins):
    dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, t + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i][j] += dp[i - coin][j - 1]

    return dp[n][t]


print(coinChangeExactlyTCoins(7, 3, [1, 2, 3, 5]))  # 9
