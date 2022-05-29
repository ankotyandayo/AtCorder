N = int(input())
x_y = []
for i in range(N):
    x, y = map(int, input().split())
    x_y.append([x, y])

for i in range(N):
    for k in range(i+1, N):
        for j in range(k+1, N):
            x1, y1 = x_y[i][0], x_y[i][1]
            x2, y2 = x_y[k][0], x_y[k][1]
            x3, y3 = x_y[j][0], x_y[j][1]
            if (x3-x1)*(y2-y1) == (y3-y1)*(x2-x1):
                print("Yes")
                exit()
print("No")
# 入力例
# 4
# 0 1
# 0 2
# 0 3
# 1 1
# 出力
# Yes
# https://atcoder.jp/contests/abc181/tasks/abc181_c
# (dy3-dy1)*(dx2-dx1) = (dx3-dx1)*(dx2-dx1)
