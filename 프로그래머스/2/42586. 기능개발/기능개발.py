def solution(progresses, speeds):
    answer = []
    left = []
    
    # 각 작업의 남은 일수를 계산
    for p, s in zip(progresses, speeds):
        days_left = (100 - p) // s if (100 - p) % s == 0 else (100 - p) // s + 1
        left.append(days_left)
    
    # 배포 날짜와 배포 개수 초기화
    current_release_day = left[0]
    cnt = 0
    
    for days in left:
        if days <= current_release_day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            current_release_day = days
    
    # 마지막 배포 개수를 추가
    answer.append(cnt)
    
    return answer