def solution(array):
    num = list(set(array))
    cnt = 0
    maxnum = array.count(num[0])
    answer = num[0]
    
    for i in num[1:]: 
        tmp = array.count(i) # 개수
        if tmp > maxnum:
            maxnum = tmp # 업데이트
            answer = i
            cnt = 0
            
        elif tmp == maxnum: # 최빈값 & 개수 같을 때
            cnt = 1
    
    if cnt == 1:
        return -1
    else:
        return answer
        
        