def solution(names):
    stack = []
    for i, name in enumerate(names):
        if i % 5 == 0:
            stack.append(name)
        
    return stack