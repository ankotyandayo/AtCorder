N, X = map(int, input().split())
X *= 100
intake = 0

for i in range(1, N+1):
    V, P = map(int, input().split())
    intake += V*P
    if X < intake:
        print(i)
        exit()

print(-1)


# https://atcoder.jp/contests/abc189/tasks/abc189_b
# 入力例
# 2 15
# 200 5
# 350 3
# 出力
# 2
