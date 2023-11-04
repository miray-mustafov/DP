def fib(n):
    # Base cases
    if n == 0:
        return 0
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


# Top-down dynamic programming (recursion + memoization)
def fib_top_down(n):
    memo = {}  # Dictionary to store memoization results
    return fib_top_down_helper(n, memo)


def fib_top_down_helper(n, memo):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    if n in memo:
        return memo[n]

    # Recursive calls with memoization
    memo[n] = fib_top_down_helper(n - 1, memo) + fib_top_down_helper(n - 2, memo)
    return memo[n]


# Bottom-up dynamic programming (forward)
def fib_bottom_up_dp_forward(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    dp = [0] * (n + 1)  # List to store dynamic programming results
    dp[1] = 1

    # Populate the list from smaller subproblems to larger ones
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# Bottom-up dynamic programming (backward)
def fib_bottom_up_dp_backward(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    dp = [0] * (n + 2)  # List to store dynamic programming results
    dp[1] = 1

    # Populate the list from smaller subproblems to larger ones
    for i in range(1, n):
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]
    return dp[n]


result = fib(10)
print(result)

result = fib_top_down(10)
print(result)

result = fib_bottom_up_dp_forward(10)
print(result)

result = fib_bottom_up_dp_backward(10)
print(result)
