N = int(input())
a = list(map(int,input().split()))
vol = [False] * (N+2)
sold = 0
sold_1 = 0

for i in range(N):
    if a[i] >= N:
        sold += 1
    elif vol[a[i]]:
        sold += 1
    else:
        vol[a[i]] = True
    
L = 1
R = N+1

while True:
    while vol[i]:
        i += 1
    if sold >= 2:
        sold -= 2
        i += 1
        vol[i] = True
    else:
        if R <= L:
            break
        elif vol[R]:
            sold += 1
            R -= 1
    break
            
print(i)
        



# # set型　{}重複される値を取り除いてくれる

# N=int(input())
# A=set(map(int,input().split()))

# l=0
# r=N+1
# while r-l>1:
#   m=(l+r)//2
#   # m巻まで読めるか?
#   c=len(set(range(1,m+1))&A) # &積集合(かぶっているやつだけ取得)ほかに対象差集合とかある
#   if c+(N-c)//2>=m: l=m
#   else: r=m

# print(l)

# 7
# 1 2 4 6 7 7 271




# https://atcoder.jp/contests/abc271/tasks/abc271_c
# https://atcoder.jp/contests/abc271/editorial/4937