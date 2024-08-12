def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 만약 k가 남아있으면 뒤에서부터 자른다
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)