'''
Problen: Coin Change
Denominations: int[] (in the example [1,2,3,5])
What are the number of ways to return change n by using even num of coins? (similar to fence of science)
1 , 2 , 3 , 5 | 0 = odd  1 = even
F(0,0) = 0, F(0,1) = 1
F(1,0) = 1, F(1,1) = 0
F(2,0) = 1, F(2,1) = 1
F(3,0) = 2, F(3,1) = 2       3,0(1,1,1 and 3)
F(4,0) = 3, F(4,1) = 4              4,1(121 112 211)
F(5,0) = 8, F(5,1) = 6

F(i,x) = F(i-coin, 1-x)+F(i-next_coin, 1-x) ...
'''


def coinChangeEvenCoins(n, coins):
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]

    # odd = 0, even = 1
    dp[0][0] = 0
    dp[0][1] = 1
    for i in range(1, n + 1):
        for x in range(2):
            for coin in coins:
                if i - coin >= 0:
                    dp[i][x] += dp[i - coin][1 - x]

    return dp[n][1]


coins = [1, 2, 3, 5]
coins2 = [1, 3, 5, 10]
n = 6
print(coinChangeEvenCoins(n, coins))
print(coinChangeEvenCoins(n, coins2))
print(coinChangeEvenCoins(4, [1, 3, 5, 10]))  # 3

print(coinChangeEvenCoins(6, [1, 3, 5, 10]))  # 8
# (1,1,1,1,1,1), (1,1,1,3), (1,1,3,1), (1,3,1,1), (3,1,1,1), (3,3), (1,5), (5,1)
# Next we will find the distinct number of ways to make a change
# (1,1,1,3), (1,1,3,1), (1,3,1,1), (3,1,1,1) => 1 way
