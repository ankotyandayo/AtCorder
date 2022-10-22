H,W = map(int,input().split())
ans = [0] * W
for i in range(H):
    C = list(input())
    for k in range(W):
        if C[k] == "#":
            ans[k] += 1
print(*ans)