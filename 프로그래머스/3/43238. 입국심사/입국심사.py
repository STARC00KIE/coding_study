def cnt_people(t, times, n): # 사람 세는 알고리즘, 목표로 하는 시간보다 같거나 적게 걸리면 True 반환
    people = 0
    for time in times:
        people += t // time
    return people >= n

def solution(n, times):
    # 초기 설정
    left = 1 # 최소 걸리는 시간
    right = max(times) * n # 최대 걸리는 시간, 제일 많이 걸리는 사람
    answer = right # 최대 걸리는 시간이 정답이므로 초기값은 right
    
    # 이분탐색
    while left <= right:
        mid = (left + right) // 2 # 목표로 하는 값
    
        if cnt_people(mid, times, n): # 목표로 하는 사람수 보다 많은 사람을 확인할 수 있으면
            right = mid - 1 # 반으로 줄여보기
            answer = mid
        else: # 목표로 하는 사람수 보다 많은 사람을 확인할 수 있으면
            left = mid + 1
    return answer