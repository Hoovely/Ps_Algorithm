# 백준_4811_다이나믹이 뭐예요?_DP_실버 2

n, m = map(int, input().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]

print(dp[n][m] % 1000000007)
