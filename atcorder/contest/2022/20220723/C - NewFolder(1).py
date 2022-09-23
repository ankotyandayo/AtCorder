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

# 5
# newfile
# newfile
# newfolder
# newfile
# newfolder

# https://atcoder.jp/contests/abc261/tasks/abc261_c

x = {'A':1,'B':2}
print(2 in x.keys)
print('B' in x.values)