def solution(people, limit):
    people.sort()  # 사람들을 몸무게 순으로 정렬합니다.
    i, j = 0, len(people) - 1  # 양 끝 포인터 초기화
    answer = 0
    
    while i <= j:
        if people[i] + people[j] <= limit:  # 가장 가벼운 사람과 가장 무거운 사람을 함께 태울 수 있으면
            i += 1  # 가벼운 사람을 다음으로
        j -= 1  # 무거운 사람을 보트에 태우고 인덱스 감소
        answer += 1  # 보트 하나 사용
    
    return answer