import heapq
N,X,Y,Z = map(int,input().split())
Ain = list(map(int,input().split()))
Bin = list(map(int,input().split()))
A = [n+10 for n in Ain] 
B = [n+10 for n in Bin] 
C = []
ans = []
passed = []

for i in range(X):
    Amax = A.index(max(A))
    if Amax not in passed:
        ans.append(Amax+1)
        A[Amax] -= 200
        B[Amax] -= 200
        passed.append(Amax)
for i in range(Y):
    Bmax = B.index(max(B))
    if Bmax not in passed:
        ans.append(Bmax+1)
        B[Bmax] = -200
        passed.append(Bmax)
        
for i in range(N):
    C.append(A[i] + B[i])
for i in range(Z):
    Cmax = C.index(max(C))
    if Cmax not in passed:
        ans.append(Cmax+1)
        C[Cmax] = -200
        passed.append(Cmax)
ans.sort()  
for i in ans:
    print(i)
