def solution(s):
    stack = []
    for c in s: # 문자열 길이 반복문
        if not stack: # 아무것도 없을 때
            stack.append(c)
        else:
            if stack[-1] == c: # 짝지어져 있을 때
                stack.pop()
            else: # 짝지어져 있지 않을 때
                stack.append(c)
    if stack: # stack 안에 뭔가 존재할 때
        answer = 0
    else:
        answer = 1
    return answer