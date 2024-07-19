def solution(participant, completion):
    dict = {}
    
    # 선수 이름 수로 정렬
    for p in participant:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1

    # 완주자 한명씩 제거
    for c in completion:
        if c in dict:
            dict[c] -= 1
            
    # 미완주자 찾기
    for key in dict.keys():
        if dict[key] > 0:
            return key
        
