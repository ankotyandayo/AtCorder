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
    for shift in range(N):
        if i >> shift == 1:
            cost += C[shift]
            for j in range[M]:
                skill[M] += A[shift][M]
    if X <= min(skill):
        ans = min(ans,cost)
if ans == 10 * 20:
    print('-1')
else:
    print(ans)
            
            

# 3 3 10
# 60 2 2 4
# 70 8 7 9
# 50 2 3 9

    