import math

graph = [[0] * 10 for _ in range(10)]

graph[0][1] = 1
graph[0][2] = 2
graph[0][3] = 3

graph[1][4] = 2
graph[1][5] = 1
graph[1][6] = 1

graph[2][4] = 1
graph[2][5] = 2
graph[2][6] = 1

graph[3][4] = 2
graph[3][5] = 3
graph[3][6] = 2

graph[4][7] = 3
graph[4][8] = 2

graph[5][7] = 3
graph[5][8] = 3

graph[6][7] = 1
graph[6][8] = 3

graph[7][9] = 4
graph[8][9] = 3

def shortest_path(graph):
    if not graph:
        return 0

    n = len(graph)
    dp = [math.inf] * n

    dp[-1] = 0
    for i in range(n - 2, -1, -1):
        for j in range(len(graph[i])):
            weight = graph[i][j]
            if weight > 0:
                dp[i] = min(dp[i], weight + dp[j])

    return dp[0]

print(shortest_path(graph))

