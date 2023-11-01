'''
Problem:
    Paint Fence with two colors:
    There is a fence with n posts, each post can be painted with green or blue.
    You have to paint the fence such that no more than two adjacent posts have the same color.
    Return the total num of ways to paint the fence.

Define objective function: F(i,j) = total num of ways to paint i posts ending with a post painted in j
'''


def numWays(n):
    dp = [[0 for j in range(2)] for i in range(n + 1)]

    # blue = 0, green = 1
    # Base cases
    dp[1][0] = 1
    dp[1][1] = 1
    dp[2][0] = 2  # 10,00
    dp[2][1] = 2  # 01,11
    for i in range(3, n + 1):
        for j in range(2):
            dp[i][j] = dp[i - 1][1 - j] + dp[i - 2][1 - j]

    return dp[n][0] + dp[n][1]


n = 4
print(numWays(n))
