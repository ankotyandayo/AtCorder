from re import A


def main():
    s = input()
    A = runLengthEncode(s)
    ans = gather(A)

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

def gather(A):
    

main()
        