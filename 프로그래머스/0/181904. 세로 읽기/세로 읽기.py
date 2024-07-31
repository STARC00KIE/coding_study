def solution(my_string, m, c):
    answer = ""
    if m == c:
        c = 0
    for i, s in enumerate(my_string):
        if (i+1) % m == c:
            answer += s
            
    print(answer)
    return answer