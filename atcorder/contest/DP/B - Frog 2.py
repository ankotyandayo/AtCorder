N,K = map(int,input().split())
h = [0] + list(map(int,input().split()))
dp = [10**15]*(N+1)

dp[1] = 0

for i in range(1,N+1):
    for k in range(1,K+1):
        if i < k:
            break
        dp[i] = min(dp[i], abs(h[i] - h[k]) + dp[k])
        
print(dp[N])








# https://atcoder.jp/contests/dp/tasks/dp_b