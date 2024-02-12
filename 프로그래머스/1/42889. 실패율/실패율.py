def solution(N, stages):
    challenger = [0] * (N + 2)
    answer = []

    # 도전자 수 구하기
    for stage in stages:
        challenger[stage] += 1
    
    # 스테이지에 실패한 사용자 수계산
    fails = {}
    total = len(stages)

    # 스테이지 순회하여 실패율 계산
    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]

    # 실패율이 높은 스테이지부터 내림차순 정렬
    result = sorted(fails, key=lambda x : fails[x], reverse=True)
    return result