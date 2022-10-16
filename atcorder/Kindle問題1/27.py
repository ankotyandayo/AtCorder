N,M=map(int, input().split())

connect=[[] for i in range(N+1)]

for i in range(M):
    A,B=map(int, input().split())
    connect[A].append(B)

from collections import deque

def BFS(start):
    visited=[False]*(N+1)

    visited[start]=True
    cnt=1

    que=deque()
    que.append(start)

    while 0<len(que):
        now_city=que.popleft()

        for to_city in connect[now_city]:
            if visited[to_city]==False:
                visited[to_city]=True
                cnt+=1
                que.append(to_city)

    return cnt

ans=0

for i in range(1,N+1):
    ans+=BFS(i)

print(ans)

# 3 3
# 1 2
# 2 3
# 3 2

N,M = map(int,input().split())
connect = [[] for i in range(N+1)]

for i in range(M):
    A,B = map(int,input().split())
    connect[A].append(B)

count = 0
for i in range(1,N+1):
    BFS = [False] ** N
    
    for k in range(connect[i]):
        if BFS[k] == False:
            count += 1
            BFS[k] = True
        
        

