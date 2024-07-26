def solution(a, d, included):
    answer = 0
    for i, b in enumerate(included):
        if b: # true일 때
            answer += i*d +a
    return answer