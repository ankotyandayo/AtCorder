N = int(input())
mountains = []
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    mountains.append([T, S])

mountains.sort(reverse=True)
print(mountains[1][1])


# 入力例
# 4
# Kita 3193
# Aino 3189
# Fuji 3776
# Okuhotaka 3190
