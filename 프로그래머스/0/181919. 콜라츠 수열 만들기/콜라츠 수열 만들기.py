
def even(n):
    return n//2   

def odd(n):
    return 3*n+1

def solution(n):
    answer = [n]
    while True:
        if n%2 == 0:
            n = even(n)
            answer.append(n)
        else:
            n = odd(n)
            answer.append(n)
        
        if n == 1:
            break
    return answer