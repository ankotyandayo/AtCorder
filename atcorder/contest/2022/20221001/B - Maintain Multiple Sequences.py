N,Q = map(int,input().split())
list_a = []
list_st = []
for i in range(N):
    t = list(map(int,input().split()))
    list_a.append(t[1:])
    
for i in range(Q):
    s,t = map(int,input().split())
    print(list_a[s-1][t-1])

# 3 4
# 4 128 741 239 901
# 2 1 1
# 3 314 159 26535
# 1 1
# 2 2
# 3 3
# 1 4
