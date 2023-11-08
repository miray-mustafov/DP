'''
Lecture 15: Coin Change (Unique Ways)
Obj Func: F(i,t) is the total num of unique ways to make a change of size i (when the last coin <= t)
Transition function:
    i >= 1: f[i][1] = f[i-1][1]
    i >= 2: f[i][2] = f[i-1][1] + f[i-2][2]
    i >= 3: f[i][3] = f[i-1][1] + f[i-2][2] + f[i-3][3]
    i >= 5: f[i][5] = f[i-1][1] + f[i-2][2] + f[i-3][3] + f[i-5][5]
'''


def coinChangeUnique(n, coins):
    dp = [[0 for _ in range(len(coins))] for _ in range(n + 1)]

    for i in range(len(coins)):
        dp[0][i] = 1

    for i in range(n + 1):
        for j in range(len(coins)):
            for k in range(j + 1):
                if i - coins[k] < 0:
                    continue
                dp[i][j] += dp[i - coins[k]][k]

    return dp[n][len(coins) - 1]


n = 4
coins = [1, 2, 3, 5]
print(f'Unique ways to make a change {n} is {coinChangeUnique(n, coins)}')
