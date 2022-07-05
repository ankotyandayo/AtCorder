N = int(input())
ans = ""
A = [ list(map(int,input())) for i in range(N)]
max = max(A[2])
index = A.index(max(A[2]))

print(max)
print(index)