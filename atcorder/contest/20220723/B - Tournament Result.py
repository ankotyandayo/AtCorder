N = int(input())
A = []
for i in range(N):
    T = list(map(str,input()))
    A.append(T)

for i in range(N):
    for k in range(N):
        if A[i][k] == "W":
            if A[k][i] != "L":
                print("incorrect")
                exit()
        elif A[i][k] == "L":
            if A[k][i] != "W":
                print("incorrect")
                exit()
        else:
            if A[k][i] != A[i][k]:
                print("incorrect")
                exit()
print("correct")