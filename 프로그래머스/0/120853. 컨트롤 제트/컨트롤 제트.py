def solution(s):
    string = list(s.split(" "))
    answer = 0
    for i, s in enumerate(string):
        if s== 'Z':
            answer -= int(string[i-1])
        else:
            answer += int(s)
    return answer