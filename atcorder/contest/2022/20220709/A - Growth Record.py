N,M,X,T,D = map(int,input().split())

if M >= X:
    print(T)
else:
    s = X - M
    ans = T - (s * D)
    print(ans)