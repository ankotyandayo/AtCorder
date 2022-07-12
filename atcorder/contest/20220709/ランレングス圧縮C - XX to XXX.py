
# ランレングス圧縮

from unittest import result


S = input()
T = input()

def encode_runlength(s):
    result = []
    p = s[0]
    a = 1
    for c in s[1:]:
        if p == c:
            a += 1
            continue
        result.append((p,a))
        p = c
        a = 1
    result.append((p,a))
    return result
            
s = encode_runlength(S)
t = encode_runlength(T)
  
if len(s) != len(t):
    print('No')
    exit()
 
for (s0, s1), (t0, t1) in zip(s, t):
    if s0 != t0:
        print('No')
        exit()
    if s1 >= 2 and t1 > s1:
        s1 = t1
    if s1 != t1:
        print('No')
        exit()

print('Yes')