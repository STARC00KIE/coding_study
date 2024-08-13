def solution(array, n):
    stack = []
    
    for a in array:
        if not stack:
            stack.append(a)
            stack.append(abs(a - n))
        else:
            if abs(a-n) < stack[1]: # 더 가까운 수
                stack[0] = a
                stack[1] = abs(a-n)
            elif abs(a-n) == stack[1]:
                if a < stack[0]:
                    stack[0] = a
        print(stack)
    return  stack[0]