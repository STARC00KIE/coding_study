def solution(n):
    num = 1 
    while (num**2) <= n:
        if n == num**2:
            return 1
        num +=1
    
    return 2