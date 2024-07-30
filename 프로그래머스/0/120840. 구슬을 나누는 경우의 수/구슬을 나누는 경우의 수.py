def solution(balls, share):
    n1 = 1
    n2 = 1
    n3 = 1
    for i in range(balls):
        n1 *= (i+1)
        
    for i in range(balls-share):
        n2 *= (i+1)
    
    for i in range(share):
        n3 *= (i+1)
    
    answer = n1/(n2*n3)
    return answer