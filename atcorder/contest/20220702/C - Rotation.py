N,Q = map(int,input().split())
S = input()

S = list(S)

for i in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        S[0:x] = S[x*-1:]
        del S[x*-1:]
    else:
        print(S[x-1])
        

# 1　末尾を先頭に x回行う
# 2  Sのx番目の文字を出力

['d', 's', 'u', 'c', 'c', 'x', 'u', 'l', 'n', 'l']
['d', 's', 'u', 'c', 'c', 'x', 'u', 'l', 'n', 'l']
['l', 'd', 's', 'u', 'c', 'c', 'x', 'u', 'l', 'n']
['l', 'd', 's', 'u', 'c', 'c', 'x', 'u', 'l', 'n']
['n', 'l', 'd', 's', 'u', 'c', 'c', 'x', 'u', 'l']
['l', 'n', 'l', 'd', 's', 'u', 'c', 'c', 'x', 'u']
['u', 'l', 'n', 'l', 'd', 's', 'u', 'c', 'c', 'x']
['u', 'l', 'n', 'l', 'd', 's', 'u', 'c', 'c', 'x']