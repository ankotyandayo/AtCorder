L1,R1,L2,R2 = map(int,input().split())
ans = 0
if R2 > L2:
    for i in range(L1,R1):
        for k in range(L2,R2):
            if i == k:
                ans += 1
print(0)
    
    
# 3,6,4,5