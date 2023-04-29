from sys import stdin

def solution(S):

    nS = len(S)
    flag = 0
    ins_pos = []
    for i in range(1,nS):
        
        if (S[i] > S[i-1]):
            flag = 1
            break
    if (flag == 0):
        return ins_pos

    # the case to dubplicate
    pre = S[0]
    count = 1
    for i in range(1,nS):
        
        
        if (pre > S[i]):
            count = 1
            pre = S[i]
            continue
        else:
            if (pre == S[i]):
                count = count + 1
            if (pre < S[i]):
                
                j = i - count
                k = 0
                while (k<count):
                    ins_pos.append(j)
                    j = j + 1
                    k = k + 1
                count = 1
        pre = S[i]
    return ins_pos

def solution_wrapper():
    T = stdin.readline()
    for i in range(int(T)):
        S =  stdin.readline()
        S = S.strip()
        ST  = ''
        RES = solution( S)
        if (len(RES) == 0):
            ST = S
        else:
            
            ns = len(S)
            for j in range(ns):
                ST = ST + S[j]
                if j in RES:
                    ST = ST + S[j]
            
        print("Case #%d: %s" % (i + 1, ST))           
if __name__ == "__main__":
    solution_wrapper()