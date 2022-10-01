N = int(input())
a = list(map(int,input().split()))
def ans(N,a):
    len_a = len(a)
    if len_a == 2:
        if a[0] == 1:
            if a[1] == 2:
                return(2)
            return(1)
    if len_a < 2:
        if a[0] == 1:
            return(1)
        return(0)
    for i in range(1,N+1):
        if a[i-1] != i:
            if len_a - i > 2:
                len_a -= 2
                continue
            else:
                return i
        else:
            len_a += 1
print(ans(N,a))

# 1
# 5
