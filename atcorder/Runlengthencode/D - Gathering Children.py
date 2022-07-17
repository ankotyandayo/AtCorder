from itertools import count
from re import A


def main():
    s = input()
    leng = len(s)
    A = runLengthEncode(s)
    ans = gather(A,leng)
    print(ans)

def runLengthEncode(s):
    b = s[0]
    c = 1
    A = []
    for i in s[1:]:
        if i == b:
            c += 1
            continue
        A.append((i,c))
        b = i
        c = 1
    return A  

def gather(A,leng):
    N = len(A)
    ans = [0] * leng 
    count = 0
    for i in range(0,N,2):
        R = A[i][1]
        L = A[i+1][1]
        count += A[i][1] + A[i+1][1]
        children1 = (A[i][1] + A[i+1][1]) // 2
        children2 = children1 + 1
        # R + Lの数が偶数
        if (count) % 2 == 0:
            ans[count-L-1] = children1
            ans[count-L] = children1
        # R + Lの数が奇数
        else:
            if R > L:
                ans[count-L-1] = children1
                ans[count-L] = children2
            else:
                ans[count-L-1] = children2
                ans[count-L] = children1
        return ans
            
            
        
    

main()
        