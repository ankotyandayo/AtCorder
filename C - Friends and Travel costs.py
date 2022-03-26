N, K = map(int, input().split())
mura_kane = []
final_village = K

for i in range(N):
    A, B = map(int, input().split())
    mura_kane.append([A, B])

mura_kane.sort()

for i in range(N):
    if mura_kane[i][0] <= final_village:
        final_village += mura_kane[i][1]
    else:
        break
print(final_village)

# 入力例
# 2 3
# 2 1
# 5 10
# 出力
# 4
