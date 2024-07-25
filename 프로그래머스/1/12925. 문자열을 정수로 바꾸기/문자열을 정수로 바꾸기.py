def solution(s):
    if s.isdigit(): # 숫자인지 판별하는 함수
        answer = int(s)
    elif s[0] == "+": # +일 때
        answer = int(s[1:])
    elif s[0] == "-": # -일 때
        answer = 0 - int(s[1:])
    return answer