# 方針 
# 変数で通常状態か反転状態かを記録しておく



S = input()
Q = int(input())
flg = False
Query = []
from collections import deque
S_deque = deque()

for i in range(len(S)):
    S_deque.append(S[i])

for i in range(Q):
    Query = list(map(str,input().split()))
    if Query[0] == "1":
        if flg == False:
            flg = True
        else:
            flg = False
    else:
        if flg == True:
            if Query[1] == "1":
                S_deque.append(Query[2])
            else:
                S_deque.appendleft(Query[2])
        else:
            if Query[1] == "1":
                S_deque.appendleft(Query[2])
            else:
                S_deque.append(Query[2])
ans = "".join(S_deque)
if flg == True:
    # 文字列の反転
    ans = ans[::-1]
    
print(ans)
                
            

# https://atcoder.jp/contests/abc158/tasks/abc158_d
