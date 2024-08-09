    # 2가 하나도 없을 때: -1
    # 2가 하나 있을 때: 2
    # 2가 2개 있을 때: 2 사이 배열
    # 2가 3개 있을 때: 첫번째, 마지막 2
    
    # 2가 들어가 있는 인덱스 배열 만들기
def solution(arr):
    ind = []
    
    for i, a in enumerate(arr):
        if a == 2:
            ind.append(i)
    
    if len(ind) == 0:
        return [-1]
    elif len(ind) == 1:
        return [2]
    else:
        return arr[min(ind):max(ind)+1]
        

    
    