n = 5  # Assuming n is some integer value

# Create a 2D list with dimensions n+1
dp = [[0 for j in range(2)] for i in range(n+1)]

# Print the dp list
for i in range(len(dp)):
    print(dp[i])