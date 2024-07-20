def solution(clothes):
    # 딕셔너리 만들기
    dic = {}
    for _,cloth in clothes:
        if cloth in dic:
            dic[cloth] += 1
        else:
            dic[cloth] = 1
    
    # 계산
    answer = 1
    for _,value in dic.items():
        answer *= (value + 1) 
    answer -= 1
    return answer