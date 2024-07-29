def solution(emergency):
    dic = {}
    answer = []
    for i, e in enumerate(sorted(emergency, reverse=True)):
        dic[e] = i+1

    for num in emergency:
        answer.append(dic[num])
    return answer