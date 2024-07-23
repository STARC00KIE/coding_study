def solution(s):
    answer = 0
    n = len(s)
    for i in range(n): # 회전
        stack = []
        for j in range(n): # 문자열 내부
            c = s[(i+j)%n] # 문자열 회전
            
            if c=="(" or c=="{" or c=="[":
                stack.append(c)
            else: # ), }, ]
                if not stack: # 스택안에 아무것도 없을 때
                    break
            
                # 닫힌 괄호는 스택의 top과 맞는지 비교
                if c==")" and stack[-1]=="(":
                    stack.pop()
                elif c=="]" and stack[-1]=="[":
                    stack.pop()
                elif c=="}" and stack[-1]=="{":
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
    return answer