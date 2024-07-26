def solution(code):
    mode = 0
    answer = ""
    for i in range(len(code)):
        # 모드 설정
        if mode == 0:
            if code[i] == '1':
                mode = 1
            elif i%2 == 0:
                answer += code[i]
        elif mode == 1:
            if code[i] == '1':
                mode = 0
            elif i%2 == 1:
                answer += code[i]
    
    if not answer:
        answer = "EMPTY"
    return answer