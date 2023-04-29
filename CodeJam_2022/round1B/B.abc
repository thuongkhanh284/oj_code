from sys import stdin

def solution(A, p):
    n = len(A)
    pre_min = 0
    pre_max = 0
    
    d_min = 0
    d_max = 0
    for p in A:
        max_p = max(p)
        min_p = min(p)
        
        d = max_p - min_p
        
        max_to_min = abs(pre_max - max_p) + d
        max_to_max = abs(pre_max - min_p) + d
        
        min_to_min = abs(pre_min - max_p) + d
        min_to_max = abs(pre_min - min_p) + d
        
        
        
        
        if (d_min + min_to_min < d_max + max_to_min):
            d_min_new = d_min + min_to_min
        else:
            d_min_new = d_max + max_to_min
            
        if (d_min + min_to_max < d_max + max_to_max):
            d_max_new = d_min + min_to_max
        else:
            d_max_new = d_max + max_to_max
        
        
        pre_min = min_p
        pre_max = max_p
        
        d_min = d_min_new
        d_max = d_max_new
        
        res = d_min
        if (d_max < res):
            res = d_max

    
    return res
    

def solution_wrapper():
    T = int(stdin.readline())
    for t in range(T):
        n, p = map(int,input().split())
        A = []
        for i in range(n):
            A.append([int(x) for x in stdin.readline().split()])

        res = solution(A , p)
        print("Case #%d: %d" % (t + 1, res))


if __name__ == "__main__":
    solution_wrapper()