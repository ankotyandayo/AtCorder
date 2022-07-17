s = list(input())

for i in s:
    a = s.count(i)
    if a == 1:
        print(i)
        exit()
print("-1")