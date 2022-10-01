from csv import list_dialects
from re import T


N,Q = map(int.input().split())
list_a = []
list_st = []
for i in range(N):
    t = list(map(int,input().split()))
    list_a.append(t)
    
for i in range(Q):
    
# 3 4
# 4 128 741 239 901
# 2 1 1
# 3 314 159 26535
# 1 1
# 2 2
# 3 3
# 1 4
