N,Q = map(int,input().split())
S = input()
k = 0
S = list(S)

for i in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        k += x
    else:
        print(S[(x-k)%N-1])
        
