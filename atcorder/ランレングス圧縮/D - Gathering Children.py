s = input()
n = len(s)

log = 18
dp = [[0] * n for n in range(log)]

for i in range(n):
    dp[0][i] = i+1 if s[i] == "R" else i-1

for k in range(1, log):
    for i in range(n):
        dp[k][i] = dp[k-1][dp[k-1][i]]

ans = [0] * n
for i in dp[log-1]:
    ans[i] += 1

print(*ans)