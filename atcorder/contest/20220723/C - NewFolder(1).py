a = input()
N = int(a)
S = [0] * N
str_sum = {"": 0}

for i in range(N):
    S = input()
    if S in str_sum:
        print(S, "(", str_sum[S], ")", sep = '')
        str_sum[S] += 1
    else:
        print(S)
        str_sum[S] = 1