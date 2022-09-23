s = list(input())

for i in s:
    a = s.count(i)
    if a == 1:
        print(i)
        exit()
print("-1")

# https://atcoder.jp/contests/abc260/tasks/abc260_a
