'''
Problem: Coin Change

Denominations: 1, 3, 5, 10
What are the number of ways to return change n?
Transition function: f(n) = f(n-1) + f(n-3) + f(n-5) + f(n-10)
TF for provided coin denominations: f(n) = f(n-d_1) + f(n-d_2) + f(n-d_3) + ... + f(n-d_k),
'''


def coinChange(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i - 1]
        if i >= 3:
            dp[i] += dp[i - 3]
        if i >= 5:
            dp[i] += dp[i - 5]
        if i >= 10:
            dp[i] += dp[i - 10]

    return dp[n]


print(coinChange(6))
