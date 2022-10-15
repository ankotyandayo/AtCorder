N,M,X = map(int,input().split())
A = []
C = []
AC = []

for i in range(N):
   CA = list(map(int,input().split()))
   C.append(CA[0])
   A.append(CA[1:]) 

ans = 10 * 20

for i in range(1<<N):
    cost = 0
    skill = [0] * M
    