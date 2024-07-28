def solution(n, source=1, target=3, auxiliary=2, answer=None):
    """
    n: 원판의 개수
    source: 원판이 처음 위치한 막대
    target: 원판을 옮길 목표 막대
    auxiliary: 보조 막대
    answer: 이동 과정을 저장할 리스트
    """
    if answer is None:
        answer = []

    if n == 1:
        answer.append([source, target])
    else:
        solution(n - 1, source, auxiliary, target, answer)
        answer.append([source, target])
        solution(n - 1, auxiliary, target, source, answer)

    return answer
