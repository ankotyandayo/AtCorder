S = input()
T = input()
T_uniquie = ''.join(set(T))
T_uniquie = list(T_uniquie)

for i in T_uniquie:
  T_n = T.count(i)
  S_n = S.count(i)
  if T_n > S_n:
    if S_n < 2:
        print("No")
        exit()
print("Yes")
