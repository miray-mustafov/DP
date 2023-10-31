'''
1. Objective function: F(i,j)
2.
3.Recurrance relation: F(i,j) = F(i-1,j) + F(i,j-1)
'''

def show_matrix(matrix):
    for row in matrix:
        print(row)
    print()
def unique_paths(m, n):
    # Initialize a 2D array to store the number of unique paths
    dp = [[1] * n for _ in range(m)]

    # Fill the dp array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            show_matrix(dp)

    # The bottom-right cell will have the number of unique paths
    return dp[m - 1][n - 1]


# Example usage:
m = 3
n = 7
result = unique_paths(m, n)
print(f'Number of unique paths in a {m}x{n} matrix: {result}')