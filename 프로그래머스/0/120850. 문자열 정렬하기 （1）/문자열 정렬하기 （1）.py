def solution(my_string):
    answer = []
    for s in my_string:
        if s.isdigit():
            answer.append(int(s))
    answer.sort()
    print(answer)
    return answer