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

def stairs(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def stairs2(n):
    if n == 1 or n == 0:
        return 1
    a, b = 1, 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c


def stairs3steps(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    a, b, c = 1, 1, 2
    for i in range(3, n + 1):
        d = a + b + c
        a, b, c = b, c, d
    return d


# time O(nk) space O(n)
def stairsKsteps(n, k):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            if i - j < 0:
                break
            dp[i] += dp[i - j]
    return dp[n]


# time O(nk) space O(k)
def stairsKstepsOkspace(n, k):
    dp = [0] * k
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, k):
            if i - j < 0:
                break
            dp[i % k] += dp[(i - j) % k]
    return dp[n % k]


n = 6
k = 3
print(f'To reach {n} stairs there are {stairs(n)} ways')
print('stairs2 ' + str(stairs2(n)))
print('stairs3steps ' + str(stairs3steps(n)))
print(stairsKsteps(n, k))
print(stairsKstepsOkspace(n, k))
