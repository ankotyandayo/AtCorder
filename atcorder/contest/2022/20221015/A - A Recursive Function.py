N = int(input())
ans = N
if N == 0:
    print(1)
else:
    for i in range(1,N):
        ans *= N - i
    print(ans)

# https://atcoder.jp/contests/abc273/tasks/abc273_a