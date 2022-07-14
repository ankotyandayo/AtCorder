def main():
    N = int(input())
    p = [-1,-1,-1,0,0,1,1,1]
    q = [-1,0,1,-1,1,-1,0,1]
    A_list = []
    for i in range(N):
        A = list(input())
        A = [int(s) for s in A]    #リストの中身をstrからintに変換する
        A_list.append(A)
    
    ans = 0
    for i in range(N):
        for k in range(N):
            for v in range(8):
                now = 0
                x = i
                y = k
                for l in range(N):
                    now *= 10
                    now += A_list[x][y]
                    x = p[k]
                    y = q[k]
                    x %= N
                    x += N
                    y %= N
                    y += N
                    y %= N
                    x %= N
                ans = max(ans,now)
    print(ans)        
main()

# 入力例
# 4
# 1161
# 1119
# 7111
# 1811

# 出力
# 9786

# こういう横がつながっているのを'トーラス'っていう
