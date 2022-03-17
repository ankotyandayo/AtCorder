N, S, D = map(int, input().split())

for i in range(N):
    X, Y = map(int, input().split())
    if X < S and Y > D:
        print("Yes")
        exit()
print("No")

# 入力例
# 4 9 9
# 5 5
# 15 5
# 5 15
# 15 15
