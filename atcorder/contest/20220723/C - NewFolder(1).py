N = int(input())
S = []
for i in range(N):
    T = list(map(str,input()))
    S.append(T)
c = 0
exist = []
count = []

exist.append(S[0])
count.append(int(1))
print(S[0])

for i in S[1:]:
    if i in S:
        print("%s(%d)" %(i,count[i.index(exist)]))
        count[i.index(exist)] = count[i.index(exist)] + 1
        
    else:
        print(i)
        exist.append(i)
        count.append(int(1))
        c += 1