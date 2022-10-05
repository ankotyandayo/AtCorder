N = int(input())
# Nを16進数に変換
ans = format(N,'x')
ans = ans.upper()
if len(ans) == 1:
    ans = '0' + str(ans)
    
print(ans)