def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        intS = int(intStr[s:s+l])
        print(intS)
        if intS > k:
            answer.append(intS)
    return answer