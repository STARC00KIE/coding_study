def solution(l, r):
    answer = []
    num = 0
    
    for i in range(l,r+1):
        for j in str(i):
            if j != '0' and j != '5':
                num = 1        
        if num == 0:
            answer.append(int(i))
        num = 0
        
    if not answer:
        answer.append(-1)
    return answer