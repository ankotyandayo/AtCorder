N = int(input())
A = list(map(int,input().split()))
ans = [0] * (2*N+1)

for i,a in enumerate(A):
  ans[2*i+1] = 