# 백준15988_1, 2, 3 더하기 3_DP_실버 2

dp = [0, 1, 2, 4]
for i in range(4, 1000001):
    dp.append((dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009)

for _ in range(int(input())):
    print(dp[int(input())])
