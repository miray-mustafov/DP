import copy

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
            # show_matrix(dp)

    # The bottom-right cell will have the number of unique paths
    return dp[m - 1][n - 1]


def max_profit(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(0, m):
        for j in range(0, n):
            if i > 0 and j > 0:
                matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1])
            elif i > 0:
                matrix[i][j] += matrix[i - 1][j]
            elif j > 0:
                matrix[i][j] += matrix[i][j - 1]

    return matrix[m - 1][n - 1]


def max_profit_path(matrix):
    def track_path(matrix):
        path = []
        i, j = len(matrix) - 1, len(matrix[0]) - 1
        while not (i == 0 and j == 0):
            path.append([i, j])
            if j > 0 and i > 0:
                if matrix[i - 1][j] > matrix[i][j - 1]:
                    i -= 1
                else:
                    j -= 1
            elif j == 0:
                i -= 1
            elif i == 0:
                j -= 1
        path.append([0, 0])
        path.reverse()
        return path

    m, n = len(matrix), len(matrix[0])
    for i in range(0, m):
        for j in range(0, n):
            if i > 0 and j > 0:
                matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1])
            elif i > 0:
                matrix[i][j] += matrix[i - 1][j]
            elif j > 0:
                matrix[i][j] += matrix[i][j - 1]

    # show_matrix(matrix)
    return track_path(matrix)


m = 3
n = 7
matrix = [
    [1, 0, 0, 0, 2],
    [2, 1, 1, 1, 1],
    [5, 4, 1, 2, 1],
]
print(f'Number of unique paths: {unique_paths(m, n)}')
# Having in mind that matrix.copy() won`t make copy of the inner lists,
# we should use those 2 methods:
print(f'max_profit: {max_profit([row[:] for row in matrix])}')
print(f'max_profit_path: {max_profit_path(copy.deepcopy(matrix))}')
