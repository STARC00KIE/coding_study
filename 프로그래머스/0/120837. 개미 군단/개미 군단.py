def solution(hp):
    # 장군개미 5, 병정개미 3, 일개미 1
    answer = 0
    if hp >= 5:
        answer += (hp//5)
        hp = hp - (hp//5)*5
    if hp >= 3:
        answer += (hp//3)
        hp = hp - (hp//3)*3
    
    answer += hp
    return answer