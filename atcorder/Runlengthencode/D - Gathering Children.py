def main():
    s = input()
    runLengthEncode(s)

def runLengthEncode(s):
    b = s[0]
    c = 1
    A = []
    for i in s[1:]:
        if i == b:
            c += 1
            continue
        A.apend((i,c))
        b = i
        c = 1
        