# Searching for the minimum cost ot get to Nth stair
# 1. Define the objective func
#   f(i) nuber of ways to reach the i-th stair
# 2. Identify base cases
#   f(0) = 1
#   f(1) = 1
# 3. Recurrence relation
#   f(n) = f(n-1)+ f(n-2)
# 4. Order of computation/execution
#   bottom-up approach
# 5. Location of the answer
#   f(n)


def paidStaircase(n, p):
    dp = [0] * (n + 1)
    dp[1] = p[1]
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + p[i]
    return dp[n]
    # without new arr
    # for i in range(2, n + 1):
    #     p[i] = min(p[i - 1], p[i - 2]) + p[i]
    # return p[n]


def paidStaircaseO2space(n, p):
    a, b, c = 0, p[1], 0
    for i in range(n + 1):
        c = min(a, b) + p[i]
        a, b = b, c
    return c


def paidSt_path(n, p):
    dp = [0] * (n + 1)
    dp[1] = p[1]
    path = set()
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + p[i]
        if dp[i - 1] < dp[i - 2]:
            path.add(i - 1)
        else:
            path.add(i - 2)

    path.add(n)
    return list(path)


n = 8
#        [0, 1, 2, 3, 4, 5, 6, 7, 8]
prices = [0, 3, 2, 4, 6, 1, 1, 5, 3]
print('paidStaircase ' + str(paidStaircase(n, prices)))
print('paidStaircaseO2space ' + str(paidStaircaseO2space(n, prices)))
print('paidSt_path ' + str(paidSt_path(n, prices)))
