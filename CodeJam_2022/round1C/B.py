from sys import stdin

ERROR = -100000

def solution(A, K , t):
    
    n = len(A)
    sum = 0
    sumi = 0
    if (K == 1):
        for i in range(n):
            sum +=  A[i]
            sumi += A[i] * A[i]
        sumA2 = sum*sum
        
        
        if (sum == 0 and (sumi - sumA2) != 0):
            print("Case #%d: %s" % (t + 1, 'IMPOSSIBLE'))
            return -1
        else:
            if (sum == 0 and (sumi - sumA2) == 0):
                res = 1
                print("Case #%d: %d" % (t + 1, res))
                return 1
            else:
            
                minus = (sumi - sumA2)
                A2 = 2*sum
                if (minus % A2== 0):
                    res = minus / A2
                    print("Case #%d: %d" % (t + 1, res))
                else:
                    print("Case #%d: %s" % (t + 1, 'IMPOSSIBLE'))
                
                
            return 1
    else:
        for i in range(n):
            sum +=  A[i]
            sumi += A[i] * A[i]
        sumA2 = sum*sum
        
        if (sum == 0 and sumi != 0):
            print("Case #%d: %s" % (t + 1, 'IMPOSSIBLE'))
            return -1
            
        if (sumA2 == sumi):
            print("Case #%d: %d" % (t + 1, 0))
            return -1
        res =  (sumi -sumA2) / (2*sum)
        print("Case #%d: %d" % (t + 1, res))
        
        
    return res
    

def solution_wrapper():
    T = int(stdin.readline())
    for t in range(T):
        n, k = map(int,input().split())
        A = []
        
        A.append([int(x) for x in stdin.readline().split()])
        
        solution(A[0] , k , t)
        


if __name__ == "__main__":
    solution_wrapper()