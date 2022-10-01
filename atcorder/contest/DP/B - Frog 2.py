
# pypyでやれば行ける
N,K = map(int,input().split())
h = [0] + list(map(int,input().split()))
dp = [10**15] * (N+1)

dp[1] = 0

for i in range(1,N+1):
    for k in range(1,K+1):
        if i <= k:
            break
        dp[i] = min(dp[i], abs(h[i]-h[i-k]) + dp[i-k])
        
print(dp[N])

# 別解
N,K = map(int,input().split())
h = list(map(int,input().split()))

dp = [10 ** 15] * (N+100)
dp[0] = 0

for i in range(N):
  for k in range(1,K+1):
    if i+k >= N:
      break
    dp[i+k] = min(dp[i+k],abs(h[i]-h[i+k])+dp[i])
print(dp[N-1])

# 5 3
# 10 30 40 50 20

# https://atcoder.jp/contests/dp/tasks/dp_b

