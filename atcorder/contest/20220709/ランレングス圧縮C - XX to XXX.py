from itertools import groupby
ans == True

def runLengthEncodeToString(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

def main():
    S = input()
    T = input()
    S_length = runLengthEncodeToString(S)
    T_length = runLengthEncodeToString(T)
    
    for i in range(len(S_length)):
        if S_length[i][1] != T_length[i][1]:
            if S_length[i][1] < 2 or S_length[i][1] > T_length[i][1]:
                ans == False
                
main()
    
# ランレングス圧縮